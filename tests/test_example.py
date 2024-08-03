import os
import json
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import EXAMPLE_DATA_FILE

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_around_tests():
    # Setup: Create a fresh data file for each test
    if EXAMPLE_DATA_FILE.exists():
        EXAMPLE_DATA_FILE.unlink()
    yield
    # Teardown: Remove the data file after each test
    if EXAMPLE_DATA_FILE.exists():
        EXAMPLE_DATA_FILE.unlink()

def test_read_example_empty():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_example():
    example_data = {"name": "test", "description": "test description"}
    response = client.post("/api/v1/", json=example_data)
    assert response.status_code == 200
    assert response.json() == example_data

    # Verify the example is in the file
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == [example_data]
