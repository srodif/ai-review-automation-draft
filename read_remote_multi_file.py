from read_all_directory_files import read_directory
from read_commit import read_commit_fn
from ignore_file_read import read_ignore_file
from remove_local_directory import remove_local_directory_fn
from github import Github
import git
import json
import os


def read_remote_multi_fn(GITHUB_TOKEN_ENV, git_user_name, repo_name, source_branch, ignore_file_path):
    g = Github(GITHUB_TOKEN_ENV)
    repo = g.get_user(git_user_name).get_repo(repo_name)
    
    ignore_list = read_ignore_file(ignore_file_path)
    # print("Ignore list: ", ignore_list)
    
    # copy locally the target branch to read the file from
    os.chdir("/")
    target_repo_local_path = "target_repo_source"
    local_git_repo_path = os.path.join(target_repo_local_path, repo_name)
    # print("Local git repo path: " + local_git_repo_path)
    # Creates dirs on the current! path
    os.makedirs(local_git_repo_path, exist_ok=True)
    # clone the target repo in the local current directory
    git.Repo.clone_from(repo.clone_url, local_git_repo_path, branch=source_branch)

    repository_file_contents = read_directory(local_git_repo_path, ignore_list)
    # print("Repository file contents: ")
    # print(repository_file_contents)
    commit_contents = read_commit_fn(GITHUB_TOKEN_ENV, git_user_name, repo_name, source_branch)
    # print("Commit contents: ")
    # print(commit_contents)
    ai_input = {
        "repo_contents": repository_file_contents,
        "commit_contents": commit_contents
    }


    json_ai_input = json.dumps(ai_input, indent=4)
    print("JSON AI Input: ")
    print(json_ai_input)


    remove_local_directory_fn(target_repo_local_path)

    return json_ai_input