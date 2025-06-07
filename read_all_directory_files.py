import os
import json

def read_directory(path, ignore_list=None, base_path=""):
    """
    Recursively read a directory and return a dictionary with its content.
    The keys are the relative paths of the files and folders to the base_path.
    Any files or folders with their names present in the ignore_list will be skipped.
    """

    if ignore_list is None:
        ignore_list = []

    content = {}
    try:
        for entry in os.listdir(path):
            if entry in ignore_list:
                continue
            full_path = os.path.join(path, entry)
            rel_path = os.path.join(base_path, entry) if base_path else entry

            # If you want forward slashes:
            rel_path = rel_path.replace("\\", "/")

            if os.path.isdir(full_path):
                sub_content = json.loads(read_directory(full_path, ignore_list, rel_path))
                content.update(sub_content)
            else:
                try:
                    with open(full_path, 'r', encoding='utf-8') as file:
                        content[rel_path] = file.read()
                except Exception as e:
                    content[rel_path] = f"Error reading file: {e}"
    except Exception as e:
        print(f"Error accessing directory {path}: {e}")

    return json.dumps(content, indent=4)