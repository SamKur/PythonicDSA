import os
from pathlib import Path

def save_file(filepath, content):
    # Convert the filepath to a Path object
    path = Path(filepath)

    # Check if the parent directory exists and create it if it doesn't
    if not path.parent.exists():
        path.parent.mkdir( parents=True)

    # Save the content to the file
    with open(path, 'w') as file:
        file.write(content)

# Example usage
filepath = 'file_path_handling/export/file.txt'
content = 'Hello, World!'
save_file(filepath, content)
