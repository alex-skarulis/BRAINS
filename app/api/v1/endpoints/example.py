from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.example_service import read_examples, create_example

router = APIRouter()

class ExampleSchema(BaseModel):
    name: str
    description: str

@router.get("/")
def read_example():
    return read_examples()

@router.post("/")
def create_example_endpoint(example: ExampleSchema):
    return create_example(example.model_dump())
