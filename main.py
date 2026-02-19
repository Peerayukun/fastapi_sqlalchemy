from fastapi import FastAPI
from app.api.router import api_router
from config import settings

app = FastAPI(title="fastapi_sqlalchemy")

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Hello world"}
