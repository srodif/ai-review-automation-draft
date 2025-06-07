from read_remote_multi_file import read_remote_multi_fn
from ai_call import ai_call_fn
from git_write_multi_file import git_write_multi_file_remote_fn
import os
from dotenv import load_dotenv
load_dotenv()

#variables declaration
# remote repository variables
GITHUB_TOKEN_ENV = os.getenv("GITHUB_TOKEN")
git_user_name = os.getenv("GIT_USERNAME")
repo_name = os.getenv("REPO_NAME")
source_branch = os.getenv("REPO_SOURCE_BRANCH")
ignore_file_path = ".llmignore"
# AI call variables
chosen_model = os.getenv("AI_CHOSEN_MODEL")
system_message_content = os.getenv("AI_SYSTEM_MESSAGE_CONTENT")
# sample new branch and commit variables
sample_new_branch = os.getenv("SAMPLE_NEW_BRANCH")
sample_commit_message = os.getenv("SAMPLE_COMMIT_MESSAGE")


# AI Process start
user_message_content = read_remote_multi_fn(GITHUB_TOKEN_ENV, git_user_name, repo_name, source_branch, ignore_file_path)
# print("User message content: ")
# print(user_message_content)

ai_output = ai_call_fn(chosen_model, system_message_content, user_message_content)
# print("AI output: ")
# print(ai_output)

git_write_multi_file_remote_fn(GITHUB_TOKEN_ENV, git_user_name, repo_name, source_branch, sample_new_branch, sample_commit_message, ai_output)

# Process complete
print("Complete. AI-generated code successfully written to remote repository.")