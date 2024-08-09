from pathlib import Path

# Define the base directory as the root of the project
BASE_DIR = Path(__file__).parent.parent

# Define the data directory path
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

JSON_DATA_DIR = DATA_DIR / "json"
JSON_DATA_DIR.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

# Define the path for the example JSON file
EXAMPLE_JSON_DATA_FILE = JSON_DATA_DIR / "example.json"
