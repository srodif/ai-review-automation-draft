from github import Github
import json


def read_commit_fn(GITHUB_TOKEN_ENV, git_user_name, repo_name, source_branch):
    g = Github(GITHUB_TOKEN_ENV)
    repo = g.get_user(git_user_name).get_repo(repo_name)

    commit_output = {}

    # Get the last commit for the specified branch
    last_commit = repo.get_commits(sha=source_branch)[0]
    # print(f"Last Commit SHA: {last_commit.sha}")
    # print(f"Author: {last_commit.commit.author.name} <{last_commit.commit.author.email}>")
    # print(f"Date: {last_commit.commit.author.date}")
    # print(f"Message: {last_commit.commit.message}")

    # Get the diff for the last commit
    # print("\nCommit Diff:")
    for file in last_commit.files:
        # print(f"{file.filename}: {file.status}")  # Print the file name and its change status
        commit_output[file.filename] = { "status" : file.status}
        if file.patch:
            # print(file.patch)  # Print the actual diff if available
            commit_output[file.filename]["patch"] = file.patch 
    
    # Convert the resulting dictionary to JSON format.
    json_commit_output = json.dumps(commit_output, indent=4)
    # print(json_commit_output)
    return json_commit_output