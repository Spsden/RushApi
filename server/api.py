from sys import prefix
from fastapi import FastAPI
from .routes import router as RushRouter

app = FastAPI()

@app.get("/", tags = ["Root"])
async def root():
    return {
        "message" : " Welcome to Rush's Api"
    }

app.include_router(RushRouter, prefix = "/rush")