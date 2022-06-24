import string
from fastapi import FastAPI
from rushpure import *

app = FastAPI()


@app.get("/apkmirror/")
async def root(app_name: str, arch: str = 'all'):
    searchAppName = app_name
    searchArch = arch
    fetchedData = getApk_url(searchAppName,searchArch)
    return fetchedData
 