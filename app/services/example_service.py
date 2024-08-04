import json
from app.core.config import EXAMPLE_JSON_DATA_FILE

def read_examples():
    if EXAMPLE_JSON_DATA_FILE.exists():
        with open(EXAMPLE_JSON_DATA_FILE, "r") as file:
            return json.load(file)
    return []

def write_examples(data):
    with open(EXAMPLE_JSON_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def create_example(data):
    examples = read_examples()
    examples.append(data)
    write_examples(examples)
    return data

