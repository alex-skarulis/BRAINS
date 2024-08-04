from fastapi import APIRouter, HTTPException
from app.utils.json_utils import read_json, write_json, update_json, delete_json
from app.core.config import EXAMPLE_JSON_DATA_FILE

router = APIRouter()

@router.get("/")
def get_json():
    return read_json(EXAMPLE_JSON_DATA_FILE)

@router.post("/")
def create_json(data: dict):
    write_json(EXAMPLE_JSON_DATA_FILE, data)
    return data

@router.put("/")
def update_json_endpoint(data: dict):
    update_json(EXAMPLE_JSON_DATA_FILE, data)
    return data

@router.delete("/")
def delete_json_endpoint():
    delete_json(EXAMPLE_JSON_DATA_FILE)
    return {"message": "File deleted"}
