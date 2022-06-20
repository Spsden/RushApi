import string
from fastapi import FastAPI
from rushpure import *

app = FastAPI()


@app.get("/apkmirror/{app_name}")
async def root(app_name: str):
    searchAppName = app_name
    fetchedData = getApk_url(searchAppName)
    return fetchedData
 