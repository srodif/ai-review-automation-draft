def read_ignore_file(file_path):
    """
    Reads .llmignore file and returns a list of non-empty, non-comment lines.
    """
    ignore_list = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Ignore empty lines and comments
                if line and not line.startswith('#'):
                    ignore_list.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return ignore_list

# Example usage
if __name__ == "__main__":
    file_path = ".llmignore"  # Change this to your file path
    ignored_entries = read_ignore_file(file_path)
    print("Ignored Entries:", ignored_entries)