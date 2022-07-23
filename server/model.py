from typing import Optional
from pydantic import BaseModel

class DownloadSchema(BaseModel):
    name_and_version: Optional[str]
    icon_url : Optional[str]
    download_link_tag : Optional[str]

    # class Config:
    #     extra = {
    #         "name_and_version" : "youtube",
    #         "icon_url" : "some url",
    #         "download_link_tag" : "downloadlink"

    #     }


