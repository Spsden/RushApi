from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from utilities.search import *
from urllib.parse import unquote

router = APIRouter()
search = SearchApp()

@router.get("/appsearch/{app_name}")
async def getAppLIst(app_name : str):
    return search.searchApp(app_name)

@router.get("/searchdownloads/{path:path}")
async def getDownloadOptions(path : str):
    lol = unquote(unquote(path))
    return search.searchDownloadOptions(url_of=path)
    #{'path' : path}
    #search.searchDownloadOptions(url_of=url)
