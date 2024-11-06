from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Header

from src.services.DiskService import DiskService

disk_router = APIRouter()
disk_service = DiskService()
@disk_router.get("/get_all_videos")
async def get_all_videos(authorization: Annotated[str | None, Header()] = None):
    return await disk_service.get_user_video(user_token=authorization)
