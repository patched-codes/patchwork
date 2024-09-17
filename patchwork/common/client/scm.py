from __future__ import annotations

import functools
import hashlib
import itertools
import time
from enum import Enum
from itertools import chain

import gitlab.const
from attrs import define
from github import Auth, Consts, Github, GithubException, PullRequest
from gitlab import Gitlab, GitlabAuthenticationError, GitlabError
from gitlab.v4.objects import ProjectMergeRequest
from typing_extensions import Protocol, TypedDict

from patchwork.logger import logger


def get_slug_from_remote_url(remote_url: str) -> str:
    # TODO: consider using https://github.com/nephila/giturlparse instead
    if remote_url.startswith("git@"):
        # ssh
        _, _, potential_slug = remote_url.partition(":")
    else:
        potential_slug = "/".join(remote_url.split("/")[-2:])

    if potential_slug.endswith(".git"):
        potential_slug = potential_slug[:-4]

    return potential_slug


@define
class Comment:
    path: str
    body: str
    start_line: int | None
    end_line: int


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
    OPEN = (["open"], ["opened"])
    CLOSED = (["closed"], ["closed", "merged"])

    def __init__(self, github_state: list[str], gitlab_state: list[str]):
        self.github_state: list[str] = github_state
        self.gitlab_state: list[str] = gitlab_state


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
                url=pr.url(), diff_anchor=diff_anchor, start_line=start, end_line=end
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
        return dict(
            title=self._pr.title or "",
            body=self._pr.body or "",
            comments=[
                dict(user=comment.user.name, body=comment.body)
                for comment in itertools.chain(self._pr.get_comments(), self._pr.get_issue_comments())
            ],
            # None checks for binary files
            diffs={file.filename: file.patch for file in self._pr.get_files() if file.patch is not None},
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

    def get_pr_by_url(self, url: str) -> PullRequestProtocol | None:
        slug, pr_id = self.get_slug_and_id_from_url(url)
        return self.find_pr_by_id(slug, pr_id)

    def find_pr_by_id(self, slug: str, pr_id: int) -> PullRequestProtocol | None:
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
    ) -> PullRequestProtocol:
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

    def get_pr_by_url(self, url: str) -> PullRequestProtocol | None:
        slug, pr_id = self.get_slug_and_id_from_url(url)
        return self.find_pr_by_id(slug, pr_id)

    def find_pr_by_id(self, slug: str, pr_id: int) -> PullRequestProtocol | None:
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
    ) -> list[PullRequestProtocol]:
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
    ) -> PullRequestProtocol:
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
