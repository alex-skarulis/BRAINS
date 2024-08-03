# Placeholder for Pydantic schemas
from pydantic import BaseModel

class ExampleSchema(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode: True
