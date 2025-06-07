from remove_local_directory import remove_local_directory_fn
from github import Github
import git
import time
import gc
import os


def git_write_multi_file_remote_fn(GITHUB_TOKEN_ENV, git_user_name, repo_name, repo_source_branch, sample_new_branch, sample_commit_message, flattened_sample_ai_output):
    # getting remote repo
    g = Github(GITHUB_TOKEN_ENV)
    repo = g.get_user(git_user_name).get_repo(repo_name)
 

    # create the path for the local clone of the repository
    os.chdir("/")
    local_repo_path = os.path.join("ai_source_multifile", repo_name)
    os.makedirs(local_repo_path, exist_ok=True)


    # clone the remote repository
    git.Repo.clone_from(repo.clone_url, local_repo_path, branch=repo_source_branch)
    # initialize the local repository
    local_repo = git.Repo(local_repo_path)
    local_repo.git.checkout("-b", sample_new_branch)


    #write the AI-generated code (using flattened structure) locally and add files to index
    os.chdir(local_repo_path)
    for file_path, file_content in flattened_sample_ai_output.items():
      dir_name = os.path.dirname(file_path)
      if dir_name:
        os.makedirs(dir_name, exist_ok=True)
      with open(file_path, "w") as f:
        f.write(file_content)
      local_repo.index.add([file_path])
      print("File " + file_path + " written successfully in " + os.getcwd())
    
    
    # commit and push the changes to the remote repository
    local_repo.index.commit(sample_commit_message)
    local_repo.git.push("origin", sample_new_branch)
    # If you want to push changes to the remote branch, it must not exist.
    # If it already exists for the same source branch, it will have the error:
    # Updates were rejected because the tip of your current branch is behind its remote counterpart.
    # If you want to update the remote branch, you can delete or merge it first.
    

    # delete local ai source directory
    os.chdir("/")
    print("Root dir? " + os.getcwd())
    local_repo.close()  # close the local repository
    del local_repo
    gc.collect()  # optionally, run garbage collection to free up memory and ensure deletion
    time.sleep(2)  # wait for a while to ensure the push and unlocks are complete
    remove_local_directory_fn("ai_source_multifile")

    return