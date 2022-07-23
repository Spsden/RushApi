from fastapi import APIRouter , Body
from fastapi.encoders import jsonable_encoder
from utilities.search import *
from server.model import DownloadSchema

router = APIRouter()
search = SearchApp()


@router.get("/app/{app_name}")
async def getAppList(app_name: str):
    return search.searchApp(app_name)




@router.get("/variants/")
async def getDownloadOptions(varianturl: str):

    return search.searchDownloadOptions(url_of=varianturl)

@router.get("/downloads/")
async def getDownloadLinks(dpageurl:str):
    return search.appInfo(url_of=dpageurl)