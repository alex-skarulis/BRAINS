import ujson as json
from pathlib import Path

def read_json(file_path):
    path = Path(file_path)
    if path.exists():
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def write_json(file_path, data):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_json(file_path, data):
    existing_data = read_json(file_path)
    existing_data.update(data)
    write_json(file_path, existing_data)

def delete_json(file_path):
    path = Path(file_path)
    if path.exists():
        path.unlink()