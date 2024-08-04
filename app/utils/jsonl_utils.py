import json
from pathlib import Path

def read_jsonl(file_path):
    path = Path(file_path)
    if path.exists():
        with open(file_path, 'r') as file:
            return [json.loads(line) for line in file]
    return []

def write_jsonl(file_path, data):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as file:
        for record in data:
            file.write(json.dumps(record) + '\n')

def append_jsonl(file_path, data):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'a') as file:
        for record in data:
            file.write(json.dumps(record) + '\n')

def delete_jsonl(file_path):
    path = Path(file_path)
    if path.exists():
        path.unlink()