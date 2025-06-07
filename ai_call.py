from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

class FileChange(BaseModel):
    file_path: str
    changes: str

class Changes(BaseModel):
    git_commit_message: str
    changed_files: list[FileChange]


def ai_call_fn(chosen_model, system_message_content, user_message_content):
    completion = client.beta.chat.completions.parse(
        model= chosen_model,
        temperature=0.0,
        messages=[
            {
                "role": "system",
                "content": system_message_content + " Change some bits in every file please!"
            },
            {
                "role": "user",
                "content": user_message_content
            }
        ],
        response_format=Changes
    )

    ai_response = completion.choices[0].message.parsed
    ai_changes = {}

    # print("Accessing commit message")
    # print(ai_response.git_commit_message)

    # print("Accessing content tests")
    # print(ai_response.changed_files[0].file_path)
    # print(ai_response.changed_files[0].changes)

    for file in ai_response.changed_files:
        ai_changes[file.file_path] = file.changes
        # print(file.file_path)
        # print(file.changes)


    # print("Printing AI changes:")
    # print(ai_changes)

    return ai_changes