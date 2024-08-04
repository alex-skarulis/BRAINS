import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import EXAMPLE_JSON_DATA_FILE

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup: Create a fresh data file for each test
    if EXAMPLE_JSON_DATA_FILE.exists():
        EXAMPLE_JSON_DATA_FILE.unlink()
    yield
    # Teardown: Remove the data file after each test
    if EXAMPLE_JSON_DATA_FILE.exists():
        EXAMPLE_JSON_DATA_FILE.unlink()

def test_get_json_empty():
    response = client.get("/api/v1/json/")
    assert response.status_code == 200
    assert response.json() == {}

def test_create_json():
    data = {"key": "value"}
    response = client.post("/api/v1/json/", json=data)
    assert response.status_code == 200
    assert response.json() == data

    response = client.get("/api/v1/json/")
    assert response.status_code == 200
    assert response.json() == data

def test_update_json():
    initial_data = {"key": "value"}
    updated_data = {"key": "new_value"}

    client.post("/api/v1/json/", json=initial_data)
    response = client.put("/api/v1/json/", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data

    response = client.get("/api/v1/json/")
    assert response.status_code == 200
    assert response.json() == updated_data

def test_delete_json():
    data = {"key": "value"}
    client.post("/api/v1/json/", json=data)

    response = client.delete("/api/v1/json/")
    assert response.status_code == 200
    assert response.json() == {"message": "File deleted"}

    response = client.get("/api/v1/json/")
    assert response.status_code == 200
    assert response.json() == {}
