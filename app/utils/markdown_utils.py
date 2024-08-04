from pathlib import Path

def read_markdown(file_path):
    path = Path(file_path)
    if path.exists():
        with open(file_path, 'r') as file:
            return file.read()
    return ""

def write_markdown(file_path, content):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)

def update_markdown(file_path, content):
    existing_content = read_markdown(file_path)
    new_content = existing_content + "\n" + content
    write_markdown(file_path, new_content)

def delete_markdown(file_path):
    path = Path(file_path)
    if path.exists():
        path.unlink()
