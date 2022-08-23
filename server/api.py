from sys import prefix
from fastapi import FastAPI
from .routes import router as RushRouter
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware



middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = ['*'],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/", tags = ["Root"])
async def root():
    return {
        "message" : " Welcome to Rush's Api"
    }

app.include_router(RushRouter, prefix = "/rush")