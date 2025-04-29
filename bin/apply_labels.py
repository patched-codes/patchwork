import os
import requests

# Define necessary environment variables and constants
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER")
REPO_NAME = os.getenv("GITHUB_REPOSITORY").split("/")[1]
PR_NUMBER = int(os.getenv("GITHUB_EVENT_NUMBER"))

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v4+json"
}

def get_linked_issues(owner, repo, pr_number):
    query = """
    query GetLinkedIssues($owner: String!, $repo: String!, $prNumber: Int!) {
      repository(owner: $owner, name: $repo) {
        pullRequest(number: $prNumber) {
          closingIssuesReferences(first: 10) {
            nodes {
              number
              labels(first: 10) {
                nodes {
                  name
                }
              }
            }
          }
        }
      }
    }
    """
    variables = {
        "owner": owner,
        "repo": repo,
        "prNumber": pr_number
    }
    response = requests.post(
        "https://api.github.com/graphql",
        headers=headers,
        json={"query": query, "variables": variables}
    )
    response.raise_for_status()
    return response.json()["data"]["repository"]["pullRequest"]["closingIssuesReferences"]["nodes"]

def apply_labels_to_pr(owner, repo, pr_number, labels):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/labels"
    data = {"labels": labels}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

def main():
    linked_issues = get_linked_issues(REPO_OWNER, REPO_NAME, PR_NUMBER)
    labels_to_add = set()

    for issue in linked_issues:
        for label in issue.get("labels", {}).get("nodes", []):
            labels_to_add.add(label["name"])

    if labels_to_add:
        apply_labels_to_pr(REPO_OWNER, REPO_NAME, PR_NUMBER, list(labels_to_add))
        print(f"Applied labels {labels_to_add} to PR #{PR_NUMBER}")
    else:
        print("No labels to apply from linked issues.")

if __name__ == "__main__":
    main()
