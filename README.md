## Running the script

With `uv` : `uv run main_script.py`

## Environment variables needed at `.env`
```
GITHUB_TOKEN=                    # Source repository token
OPENAI_API_KEY=
GIT_USERNAME=
REPO_NAME=                       # Source repository name
REPO_SOURCE_BRANCH=              # Branch to be tested / fixed
AI_CHOSEN_MODEL=
AI_SYSTEM_MESSAGE_CONTENT='You are a helpful software engineer focused on proactively fixing bugs. The user provided commit and code triggered a failed test, please fix it. Your answer should be in json format, showing the changed files and their updated content. Your answer may contain changes to multiple files.'
SAMPLE_NEW_BRANCH=               # Branch that the ai generated content will be written
SAMPLE_COMMIT_MESSAGE=
```
