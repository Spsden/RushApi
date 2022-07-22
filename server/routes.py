from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from utilities.search import *


router = APIRouter()
search = SearchApp()


@router.get("/appsearch/{app_name}")
async def getAppList(app_name: str):
    return search.searchApp(app_name)


@router.get("/searchdownloads/{path:path}")
async def getDownloadOptions(path: str):
    return search.searchDownloadOptions(url_of=path)

@router.get("/searchlinks/{path:path}")
async def getDownloadLinks(path:str):
    return search.appInfo(url_of=path)