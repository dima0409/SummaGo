from typing import Annotated

from fastapi import APIRouter, Request
from fastapi.params import Header

from services.DiskService import DiskService

DiskRouter = APIRouter(
    prefix="/v1/disk"
)
DiskService = DiskService()
@DiskRouter.get("/get_all_videos")
async def get_all_videos(authorization: Annotated[str | None, Header()] = None):
    return await DiskService.get_user_video(user_token=authorization)

@DiskRouter.get("/download_video_by_id")
async def download_video_by_id(video_id: str,authorization: Annotated[str | None, Header()] = None):
    pass