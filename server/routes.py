
from fastapi import APIRouter, Body, Response
from fastapi.encoders import jsonable_encoder
from utilities import search, searchpure
from server.model import DownloadSchema
from fastapi.responses import JSONResponse

router = APIRouter()

mirror = search.SearchApp()
pure = searchpure.SearchPure()


@router.get("/app/{app_name}")
async def getAppList(app_name: str, response: Response):
    content = pure.searchApp(query=app_name) + mirror.searchApp(query=app_name)
    #+ search.searchApp(app_name)
    response.headers["Access-Control-Allow-Origin"] = "*"

    return content
    # return content


@router.get("/variants/")
async def getDownloadOptions(varianturl: str):
    return mirror.searchDownloadOptions(url_of=varianturl)

    #return search.searchDownloadOptions(url_of=varianturl)


@router.get("/downloads/")
async def getDownloadLinks(dpageurl: str):
    return search.appInfo(url_of=dpageurl)
