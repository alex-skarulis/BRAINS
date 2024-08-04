from fastapi import FastAPI
from app.api.v1.endpoints import json_example

app = FastAPI()

app.include_router(json_example.router, prefix="/api/v1/json", tags=["json_example"])
