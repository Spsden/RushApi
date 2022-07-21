from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from utilities.search import *

router = APIRouter()
search = SearchApp()

@router.get("/{app_name}")
async def getAppLIst(app_name : str):
    return search.searchApp(app_name)
