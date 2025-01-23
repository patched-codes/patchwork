from __future__ import annotations

import functools
import hashlib
import itertools
import time
from difflib import unified_diff
from enum import Enum
from itertools import chain
from pathlib import Path

import git
import gitlab.const
from azure.devops.connection import Connection
from azure.devops.released.client_factory import ClientFactory
from azure.devops.released.core.core_client import CoreClient
from azure.devops.released.git.git_client import GitClient
from azure.devops.v7_1.git.models import (
    Comment,
    GitPullRequest,
    GitPullRequestCommentThread,
    GitPullRequestSearchCriteria,
    GitRepository,
    TeamProjectReference,
)
from github import Auth, Consts, Github, GithubException, PullRequest
from github.GithubException import UnknownObjectException
from gitlab import Gitlab, GitlabAuthenticationError, GitlabError
from gitlab.v4.objects import ProjectMergeRequest
from giturlparse import GitUrlParsed, parse
from msrest.authentication import BasicAuthentication
from typing_extensions import Iterator, Protocol, TypedDict

from patchwork.logger import logger


def get_slug_from_remote_url(remote_url: str) -> str:
    parsed_repo: GitUrlParsed = parse(remote_url)
    parts = [parsed_repo.owner, *parsed_repo.groups, parsed_repo.name]
    slug = "/".join(parts)
    return slug


class IssueText(TypedDict):
    title: str
    body: str
    comments: list[str]


class PullRequestComment(TypedDict):
    user: str
    body: str


class PullRequestTexts(TypedDict):
    title: str
    body: str
    comments: list[PullRequestComment]
    diffs: dict[str, str]


class PullRequestState(Enum):
    OPEN = (["open"], ["opened"], ["active"])
    CLOSED = (["closed"], ["closed", "merged"], ["completed", "abandoned", "notSet"])

    def __init__(self, github_state: list[str], gitlab_state: list[str], azure_devops_state: list[str]):
        self.github_state: list[str] = github_state
        self.gitlab_state: list[str] = gitlab_state
        self.azure_devops_state: list[str] = azure_devops_state


_COMMENT_MARKER = "<!-- PatchWork comment marker -->"


class PullRequestProtocol(Protocol):
    @property
    def id(self) -> int:
        ...

    def url(self) -> str:
        ...

    def set_pr_description(self, body: str) -> None:
        ...

    def create_comment(
        self, body: str, path: str | None = None, start_line: int | None = None, end_line: int | None = None
    ) -> str | None:
        ...

    def reset_comments(self) -> None:
        ...

    def texts(self) -> PullRequestTexts:
        ...

    @staticmethod
    def _get_template_indexes(template: str) -> tuple[int | None, int | None]:
        start_idx = template.find("{{")
        if start_idx == -1:
            return None, None

        end_idx = template.find("}}", start_idx)
        if end_idx == -1:
            return None, None

        return start_idx, end_idx

    @staticmethod
    def _apply_pr_template(pr: "PullRequestProtocol", body: str) -> str:
        if isinstance(pr, GithubPullRequest):
            backup_link_format = "{url}/files"
            file_link_format = backup_link_format + "#diff-{diff_anchor}"
            chunk_link_format = file_link_format + "L{start_line}-L{end_line}"
            anchor_hash = hashlib.sha256
        elif isinstance(pr, GitlabMergeRequest):
            backup_link_format = "{url}/diffs"
            file_link_format = backup_link_format + "#{diff_anchor}"
            # TODO: deal with gitlab line links
            # chunk_link_format = file_link_format + "_{start_line}_{end_line}"
            chunk_link_format = file_link_format + ""
            anchor_hash = hashlib.sha1
        elif isinstance(pr, AzureDevopsPullRequest):
            backup_link_format = "{url}?_a=files"
            file_link_format = backup_link_format + "&path=/{path}"
            chunk_link_format = file_link_format + ""
            anchor_hash = hashlib.md5
        else:
            return pr.url()

        template = body
        start_idx, end_idx = PullRequestProtocol._get_template_indexes(template)
        while start_idx is not None and end_idx is not None:
            template_content = template[start_idx + 2 : end_idx]

            split_parts = template_content.split(":")
            split_parts_iter = iter(split_parts)
            path = next(split_parts_iter, None)
            start = next(split_parts_iter, None)
            end = next(split_parts_iter, None)

            diff_anchor = ""
            format_to_use = backup_link_format
            if path is not None:
                diff_anchor = anchor_hash(path.encode()).hexdigest()
                format_to_use = file_link_format
                if start is not None and end is not None:
                    format_to_use = chunk_link_format

            replacement_value = format_to_use.format(
                url=pr.url(), path=path, diff_anchor=diff_anchor, start_line=start, end_line=end
            )
            template = template[:start_idx] + replacement_value + template[end_idx + 2 :]
            start_idx, end_idx = PullRequestProtocol._get_template_indexes(template)

        return template


class ScmPlatformClientProtocol(Protocol):
    def test(self) -> bool:
        ...

    def set_url(self, url: str) -> None:
        ...

    def get_slug_and_id_from_url(self, url: str) -> tuple[str, int] | None:
        ...

    def find_issue_by_url(self, url: str) -> IssueText | None:
        ...

    def find_issue_by_id(self, slug: str, issue_id: int) -> IssueText | None:
        ...

    def get_pr_by_url(self, url: str) -> PullRequestProtocol | None:
        ...

    def find_pr_by_id(self, slug: str, pr_id: int) -> PullRequestProtocol | None:
        ...

    def find_prs(
        self,
        slug: str,
        state: PullRequestState | None = None,
        original_branch: str | None = None,
        feature_branch: str | None = None,
        limit: int | None = None,
    ) -> list[PullRequestProtocol]:
        ...

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> PullRequestProtocol:
        ...

    def create_issue_comment(
        self, slug: str, issue_text: str, title: str | None = None, issue_id: int | None = None
    ) -> str:
        ...


class GitlabMergeRequest(PullRequestProtocol):
    def __init__(self, mr: ProjectMergeRequest):
        self._mr = mr

    @property
    def id(self) -> int:
        return self._mr.iid

    def url(self) -> str:
        return self._mr.web_url

    def set_pr_description(self, body: str) -> None:
        self._mr.description = PullRequestProtocol._apply_pr_template(self, body)
        self._mr.save()

    def create_comment(
        self, body: str, path: str | None = None, start_line: int | None = None, end_line: int | None = None
    ) -> str | None:
        final_body = f"{_COMMENT_MARKER} \n{PullRequestProtocol._apply_pr_template(self, body)}"
        if path is None:
            note = self._mr.notes.create({"body": final_body})
            return f"#note_{note.get_id()}"

        commit = None
        for i in range(3):
            try:
                commit = self._mr.commits().next()
            except StopIteration:
                time.sleep(2**i)

        if commit is None:
            return None

        diff = None
        for i in range(3):
            try:
                iterator = self._mr.diffs.list(iterator=True)
                diff = iterator.next()  # type: ignore
                if diff.head_commit_sha == commit.get_id():
                    break
            except StopIteration:
                time.sleep(2**i)
                continue

        if diff is None:
            return None

        base_commit = diff.base_commit_sha
        head_commit = diff.head_commit_sha

        try:
            discussion = self._mr.discussions.create(
                {
                    "body": final_body,
                    "position": {
                        "base_sha": base_commit,
                        "start_sha": base_commit,
                        "head_sha": head_commit,
                        "position_type": "text",
                        "old_path": path,
                        "new_path": path,
                        "old_line": end_line,
                        "new_line": end_line,
                    },
                }
            )
        except Exception as e:
            logger.error(e)
            return None

        for note in discussion.attributes["notes"]:
            return f"#note_{note['id']}"

        return None

    def reset_comments(self) -> None:
        for discussion in self._mr.discussions.list(iterator=True):
            for note in discussion.attributes["notes"]:
                if note["body"].startswith(_COMMENT_MARKER):
                    discussion.notes.delete(note["id"])

    def texts(self) -> PullRequestTexts:
        title = self._mr.title
        body = self._mr.description
        notes = [
            dict(user=note.author.get("username") or "", body=note.body)
            for note in self._mr.notes.list(iterator=True)
            if note.system is False and note.author is not None and note.body is not None
        ]

        diffs = self._mr.diffs.list()
        latest_diff = max(diffs, key=lambda diff: diff.created_at, default=None)
        if latest_diff is None:
            return dict(title=title, body=body, comments=notes, diffs={})

        files = self._mr.diffs.get(latest_diff.id).diffs
        return dict(
            title=title,
            body=body,
            comments=notes,
            diffs={file["new_path"]: file["diff"] for file in files if not file["diff"].startswith("Binary files")},
        )


class GithubPullRequest(PullRequestProtocol):
    def __init__(self, pr: PullRequest):
        self._pr: PullRequest = pr

    @property
    def id(self) -> int:
        return self._pr.number

    def url(self) -> str:
        return self._pr.html_url

    def set_pr_description(self, body: str) -> None:
        final_body = PullRequestProtocol._apply_pr_template(self, body)
        self._pr.edit(body=final_body)

    def create_comment(
        self, body: str, path: str | None = None, start_line: int | None = None, end_line: int | None = None
    ) -> str | None:
        final_body = f"{_COMMENT_MARKER} \n{PullRequestProtocol._apply_pr_template(self, body)}"

        if path is None:
            return self._pr.create_issue_comment(body=final_body).html_url

        kwargs = dict(body=final_body, path=path)
        if start_line is not None:
            kwargs["start_line"] = start_line
            kwargs["start_side"] = "LEFT"
        if end_line is not None:
            kwargs["line"] = end_line
            kwargs["side"] = "LEFT"

        return self._pr.create_review_comment(commit=self._pr.get_commits()[0], **kwargs).html_url  # type: ignore

    def reset_comments(self) -> None:
        for comment in chain(self._pr.get_review_comments(), self._pr.get_issue_comments()):
            if comment.body.startswith(_COMMENT_MARKER):
                comment.delete()

    def texts(self) -> PullRequestTexts:
        comments = []
        for comment in chain(self._pr.get_review_comments(), self._pr.get_issue_comments()):
            try:
                # Copilot user throws here
                user = comment.user.name
            except UnknownObjectException:
                user = comment.user.login

            comments.append(dict(user=user, body=comment.body))

        return dict(
            title=self._pr.title or "",
            body=self._pr.body or "",
            comments=comments,
            # None checks for binary files
            diffs={file.filename: file.patch for file in self._pr.get_files() if file.patch is not None},
        )


class AzureDevopsPullRequest(PullRequestProtocol):
    def __init__(self, pr: GitPullRequest, git_client: GitClient, pr_base_url: str):
        self._pr: GitPullRequest = pr
        self.git_client: GitClient = git_client
        self.pr_base_url = pr_base_url

    @property
    def id(self) -> int:
        return self._pr.pull_request_id

    def url(self) -> str:
        final_pr_url = self.pr_base_url
        if not final_pr_url.endswith("/"):
            final_pr_url += "/"
        return final_pr_url + str(self.id)

    def set_pr_description(self, body: str) -> None:
        final_body = PullRequestProtocol._apply_pr_template(self, body)
        body = GitPullRequest(description=final_body)
        self._pr = self.git_client.update_pull_request(
            body,
            repository_id=self._pr.repository.id,
            pull_request_id=self._pr.pull_request_id,
            project=self._pr.repository.project.id,
        )

    def create_comment(
        self, body: str, path: str | None = None, start_line: int | None = None, end_line: int | None = None
    ) -> str | None:
        try:
            comment_body = Comment(content=body)
            comment_thread_body = GitPullRequestCommentThread(comments=[comment_body])
            comment_thread = self.git_client.create_thread(
                comment_thread_body,
                repository_id=self._pr.repository.id,
                pull_request_id=self.id,
                project=self._pr.repository.project.id,
            )
            return body
        except Exception as e:
            logger.error(e)
            return None

    def __iter_comments(self) -> Iterator[tuple[GitPullRequestCommentThread, list[Comment]]]:
        threads = self.git_client.get_threads(
            repository_id=self._pr.repository.id, pull_request_id=self.id, project=self._pr.repository.project.id
        )
        for thread in threads:
            comments = self.git_client.get_comments(
                repository_id=self._pr.repository.id,
                pull_request_id=self.id,
                thread_id=thread.id,
                project=self._pr.repository.project.id,
            )
            yield thread, comments

    def reset_comments(self) -> None:
        for thread, comments in self.__iter_comments():
            comment_ids_to_delete = []
            for comment in comments:
                if comment.content is not None and comment.content.startswith(_COMMENT_MARKER):
                    comment_ids_to_delete.append(comment.id)
            if len(comment_ids_to_delete) == len(comments):
                for comment_id in comment_ids_to_delete:
                    self.git_client.delete_comment(
                        repository_id=self._pr.repository.id,
                        pull_request_id=self.id,
                        thread_id=thread.id,
                        comment_id=comment_id,
                        project=self._pr.repository.project.id,
                    )

    def texts(self) -> PullRequestTexts:
        target_branch = self._pr.last_merge_source_commit.commit_id
        feature_branch = self._pr.last_merge_target_commit.commit_id

        repo = git.Repo(path=Path.cwd(), search_parent_directories=True)
        for remote in repo.remotes:
            remote.fetch()
        target_commit = repo.commit(target_branch)
        feature_commit = repo.commit(feature_branch)

        diff_index = feature_commit.diff(target_commit)
        diffs = dict()
        for diff in diff_index:
            a_path = diff.a_path
            b_path = diff.b_path
            a_blob = diff.a_blob.data_stream.read().decode("utf-8")
            b_blob = diff.b_blob.data_stream.read().decode("utf-8")
            diff_lines = unified_diff(
                a_blob.splitlines(keepends=True), b_blob.splitlines(keepends=True), a_path, b_path
            )
            diff_content = "".join(diff_lines)
            diffs[a_path] = diff_content

        comments: list[PullRequestComment] = []
        for _, raw_comments in self.__iter_comments():
            for raw_comment in raw_comments:
                comments.append(dict(user=raw_comment.author.display_name, body=raw_comment.content))
        return dict(
            title=self._pr.title or "",
            body=self._pr.description or "",
            comments=comments,
            diffs=diffs,
        )


class GithubClient(ScmPlatformClientProtocol):
    DEFAULT_URL = Consts.DEFAULT_BASE_URL

    def __init__(self, access_token: str, url: str = DEFAULT_URL):
        self._access_token = access_token
        self._url = url

    @functools.cached_property
    def github(self) -> Github:
        auth = Auth.Token(self._access_token)
        return Github(base_url=self._url, auth=auth)

    def test(self) -> bool:
        return True

    def set_url(self, url: str) -> None:
        self._url = url

    def get_slug_and_id_from_url(self, url: str) -> tuple[str, int] | None:
        url_parts = url.split("/")
        if len(url_parts) < 5:
            logger.error(f"Invalid issue URL: {url}")
            return None

        try:
            resource_id = int(url_parts[-1])
        except ValueError:
            logger.error(f"Invalid issue URL: {url}")
            return None

        slug = "/".join(url_parts[-4:-2])

        return slug, resource_id

    def find_issue_by_url(self, url: str) -> IssueText | None:
        slug, issue_id = self.get_slug_and_id_from_url(url)
        return self.find_issue_by_id(slug, issue_id)

    def find_issue_by_id(self, slug: str, issue_id: int) -> IssueText | None:
        repo = self.github.get_repo(slug)
        try:
            issue = repo.get_issue(issue_id)
            return dict(
                title=issue.title,
                body=issue.body,
                comments=[issue_comment.body for issue_comment in issue.get_comments()],
            )
        except GithubException as e:
            logger.warn(f"Failed to get issue: {e}")
            return None

    def get_pr_by_url(self, url: str) -> GithubPullRequest | None:
        slug, pr_id = self.get_slug_and_id_from_url(url)
        return self.find_pr_by_id(slug, pr_id)

    def find_pr_by_id(self, slug: str, pr_id: int) -> GithubPullRequest | None:
        repo = self.github.get_repo(slug)
        try:
            pr = repo.get_pull(pr_id)
            return GithubPullRequest(pr)
        except GithubException as e:
            logger.warn(f"Failed to get PR: {e}")
            return None

    def find_prs(
        self,
        slug: str,
        state: PullRequestState | None = None,
        original_branch: str | None = None,
        feature_branch: str | None = None,
        limit: int | None = None,
    ) -> list[GithubPullRequest]:
        repo = self.github.get_repo(slug)
        kwargs_list = dict(state=[None], target_branch=[None], source_branch=[None])

        if state is not None:
            kwargs_list["state"] = state.github_state  # type: ignore
        if original_branch is not None:
            kwargs_list["base"] = [original_branch]  # type: ignore
        if feature_branch is not None:
            kwargs_list["head"] = [feature_branch]  # type: ignore

        page_list = []
        keys = kwargs_list.keys()
        for instance in itertools.product(*kwargs_list.values()):
            kwargs = dict(((key, value) for key, value in zip(keys, instance) if value is not None))
            pages = repo.get_pulls(**kwargs)
            page_list.append(pages)

        branch_checker = lambda pr: True
        if original_branch is not None:
            branch_checker = lambda pr: branch_checker and pr.base.ref == original_branch
        if feature_branch is not None:
            branch_checker = lambda pr: branch_checker and pr.head.ref == feature_branch

        # filter out PRs that are not the ones we are looking for
        rv_list = []
        for pr in itertools.islice(itertools.chain(*page_list), limit):
            if branch_checker(pr):
                rv_list.append(GithubPullRequest(pr))
        return rv_list

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> GithubPullRequest:
        # before creating a PR, check if one already exists
        repo = self.github.get_repo(slug)
        gh_pr = repo.create_pull(title=title, body=body, base=original_branch, head=feature_branch)
        pr = GithubPullRequest(gh_pr)
        return pr

    def create_issue_comment(
        self, slug: str, issue_text: str, title: str | None = None, issue_id: int | None = None
    ) -> str:
        repo = self.github.get_repo(slug)
        if issue_id is not None:
            return repo.get_issue(issue_id).create_comment(issue_text).html_url
        else:
            return repo.create_issue(title, issue_text).html_url


class GitlabClient(ScmPlatformClientProtocol):
    DEFAULT_URL = gitlab.const.DEFAULT_URL

    def __init__(self, access_token: str, url: str = DEFAULT_URL):
        self._access_token = access_token
        self._url = url

    @functools.cached_property
    def gitlab(self) -> Gitlab:
        return Gitlab(self._url, private_token=self._access_token)

    def set_url(self, url: str) -> None:
        self._url = url

    def test(self) -> bool:
        try:
            self.gitlab.auth()
        except GitlabAuthenticationError:
            return False
        return self.gitlab.user is not None

    def get_slug_and_id_from_url(self, url: str) -> tuple[str, int] | None:
        url_parts = url.split("/")
        if len(url_parts) < 5:
            logger.error(f"Invalid issue URL: {url}")
            return None

        try:
            resource_id = int(url_parts[-1])
        except ValueError:
            logger.error(f"Invalid issue URL: {url}")
            return None

        slug = "/".join(url_parts[-5:-3])

        return slug, resource_id

    def find_issue_by_url(self, url: str) -> IssueText | None:
        slug, issue_id = self.get_slug_and_id_from_url(url)
        return self.find_issue_by_id(slug, issue_id)

    def find_issue_by_id(self, slug: str, issue_id: int) -> IssueText | None:
        project = self.gitlab.projects.get(slug)
        try:
            issue = project.issues.get(issue_id)
            return dict(
                title=issue.get("title", ""),
                body=issue.get("description", ""),
                comments=[note["body"] for note in issue.notes.list()],
            )
        except GitlabError as e:
            logger.warn(f"Failed to get issue: {e}")
            return None

    def get_pr_by_url(self, url: str) -> GitlabMergeRequest | None:
        slug, pr_id = self.get_slug_and_id_from_url(url)
        return self.find_pr_by_id(slug, pr_id)

    def find_pr_by_id(self, slug: str, pr_id: int) -> GitlabMergeRequest | None:
        project = self.gitlab.projects.get(slug)
        try:
            mr = project.mergerequests.get(pr_id)
            return GitlabMergeRequest(mr)
        except GitlabError as e:
            logger.warn(f"Failed to get MR: {e}")
            return None

    def find_prs(
        self,
        slug: str,
        state: PullRequestState | None = None,
        original_branch: str | None = None,
        feature_branch: str | None = None,
        limit: int | None = None,
    ) -> list[GitlabMergeRequest]:
        project = self.gitlab.projects.get(slug)
        kwargs_list = dict(iterator=[True], state=[None], target_branch=[None], source_branch=[None])

        if state is not None:
            kwargs_list["state"] = state.gitlab_state  # type: ignore
        if original_branch is not None:
            kwargs_list["target_branch"] = [original_branch]  # type: ignore
        if feature_branch is not None:
            kwargs_list["source_branch"] = [feature_branch]  # type: ignore

        page_list = []
        keys = kwargs_list.keys()
        for instance in itertools.product(*kwargs_list.values()):
            kwargs = dict(((key, value) for key, value in zip(keys, instance) if value is not None))
            mrs_instance = project.mergerequests.list(**kwargs)
            page_list.append(list(mrs_instance))

        rv_list = []
        for mr in itertools.islice(itertools.chain(*page_list), limit):
            rv_list.append(GitlabMergeRequest(mr))

        return rv_list

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> GitlabMergeRequest:
        # before creating a PR, check if one already exists
        project = self.gitlab.projects.get(slug)
        gl_mr = project.mergerequests.create(
            {
                "source_branch": feature_branch,
                "target_branch": original_branch,
                "title": title,
                "description": body,
                "labels": "patchwork",
            }
        )
        mr = GitlabMergeRequest(gl_mr)  # type: ignore
        return mr

    def create_issue_comment(
        self, slug: str, issue_text: str, title: str | None = None, issue_id: int | None = None
    ) -> str:
        if issue_id is not None:
            obj = self.gitlab.projects.get(slug).issues.get(issue_id).notes.create({"body": issue_text})
            return obj["web_url"]

        obj = self.gitlab.projects.get(slug).issues.create({"title": title, "description": issue_text})
        return obj["web_url"]


class AzureDevopsClient(ScmPlatformClientProtocol):
    DEFAULT_URL = "https://dev.azure.com/"

    def __init__(self, access_token: str, url: str = DEFAULT_URL, remote: str = "origin"):
        self.credentials = BasicAuthentication("", access_token)
        self.__url = url
        self.__remote = remote
        git_repo = git.Repo(Path.cwd(), search_parent_directories=True)
        original_remote_url = git_repo.remotes[remote].url
        parsed_repo: GitUrlParsed = parse(original_remote_url)
        self.__org_name = parsed_repo.owner
        self.__project_name = parsed_repo.groups_path.replace("/_git", "")
        self.__repo_name = parsed_repo.repo

    def __pr_resource_html_url(self):
        url = self.__url
        if not url.endswith("/"):
            url += "/"
        return f"{url}{self.__org_name}/{self.__project_name}/_git/{self.__repo_name}/pullrequest/"

    @functools.cached_property
    def clients(self) -> ClientFactory:
        url = self.__url
        if not url.endswith("/"):
            url += "/"

        conn = Connection(base_url=f"{url}{self.__org_name}", creds=self.credentials)
        return conn.clients

    @functools.cached_property
    def git_client(self) -> GitClient:
        return self.clients.get_git_client()

    @functools.cached_property
    def core_client(self) -> CoreClient:
        return self.clients.get_core_client()

    @functools.cached_property
    def project(self) -> TeamProjectReference:
        projs = self.core_client.get_projects()
        proj = next((proj for proj in projs if proj.name == self.__project_name), None)
        if proj is None:
            raise ValueError(
                f"Unable to determine project name from remote {self.__remote} url. Parsed project name: {self.__project_name}"
            )
        return proj

    @functools.cached_property
    def repo(self) -> GitRepository:
        repos = self.git_client.get_repositories(project=self.project.id)
        git_repo = next((r for r in repos if r.name == self.__repo_name), None)
        if git_repo is None:
            raise ValueError(
                f"Unable to determine repository name from remote {self.__remote} url. Parsed repository name: {self.__repo_name}"
            )
        return git_repo

    def set_url(self, url: str) -> None:
        self.__url = url

    def test(self) -> bool:
        try:
            proj = self.project
            return True
        except ValueError:
            return False

    def get_slug_and_id_from_url(self, url: str) -> tuple[str, int] | None:
        url_parts = url.split("/")
        if len(url_parts) == 1:
            logger.error(f"Invalid URL: {url}")
            return None

        try:
            resource_id = int(url_parts[-1])
        except ValueError:
            logger.error(f"Invalid URL: {url}")
            return None

        slug = "/".join(url_parts[-6:-3])

        return slug, resource_id

    def find_issue_by_url(self, url: str) -> IssueText | None:
        ...

    def find_issue_by_id(self, slug: str, issue_id: int) -> IssueText | None:
        ...

    def get_pr_by_url(self, url: str) -> AzureDevopsPullRequest | None:
        slug, resource_id = self.get_slug_and_id_from_url(url)
        return self.find_pr_by_id(slug, resource_id)

    def find_pr_by_id(self, slug: str, pr_id: int) -> AzureDevopsPullRequest | None:
        pr = self.git_client.get_pull_request(
            repository_id=self.repo.id, pull_request_id=pr_id, project=self.project.id
        )
        return AzureDevopsPullRequest(pr, self.git_client, self.__pr_resource_html_url())

    def find_prs(
        self,
        slug: str,
        state: PullRequestState | None = None,
        original_branch: str | None = None,
        feature_branch: str | None = None,
        limit: int | None = None,
    ) -> list[AzureDevopsPullRequest]:
        kwargs_list = dict(status=[None], target_ref_name=[None], source_ref_name=[None])

        if state is not None:
            kwargs_list["status"] = state.gitlab_state  # type: ignore
        if original_branch is not None:
            kwargs_list["target_ref_name"] = [f"refs/heads/{original_branch}"]  # type: ignore
        if feature_branch is not None:
            kwargs_list["source_ref_name"] = [f"refs/heads/{feature_branch}"]  # type: ignore

        page_list = []
        keys = kwargs_list.keys()
        for instance in itertools.product(*kwargs_list.values()):
            kwargs = dict(((key, value) for key, value in zip(keys, instance) if value is not None))
            git_pr_search = GitPullRequestSearchCriteria(
                repository_id=self.repo.id,
                **kwargs,
            )
            pr_instances = self.git_client.get_pull_requests(
                project=self.project.id, repository_id=self.repo.id, search_criteria=git_pr_search
            )
            page_list.append(pr_instances)

        rv_list = []
        for mr in itertools.islice(itertools.chain(*page_list), limit):
            rv_list.append(AzureDevopsPullRequest(mr, self.git_client, self.__pr_resource_html_url()))

        return rv_list

    def create_pr(
        self,
        slug: str,
        title: str,
        body: str,
        original_branch: str,
        feature_branch: str,
    ) -> AzureDevopsPullRequest:
        # before creating a PR, check if one already exists
        pr_body = GitPullRequest(
            source_ref_name=f"refs/heads/{feature_branch}",
            target_ref_name=f"refs/heads/{original_branch}",
            title=title,
            description=body,
            # should be web tag definition
            # labels="patchwork",
        )
        pr_instance = self.git_client.create_pull_request(pr_body, repository_id=self.repo.id, project=self.project.id)
        mr = AzureDevopsPullRequest(pr_instance, self.git_client, self.__pr_resource_html_url())  # type: ignore
        return mr

    def create_issue_comment(
        self, slug: str, issue_text: str, title: str | None = None, issue_id: int | None = None
    ) -> str:
        ...
