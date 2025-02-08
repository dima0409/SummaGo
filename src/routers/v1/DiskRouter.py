from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.params import Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.services.DiskService import DiskService
security = HTTPBearer()
disk_router = APIRouter()
disk_service = DiskService()
@disk_router.get("/get_ all_videos")
async def get_all_videos(  credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    return await disk_service.get_user_video(user_token=credentials.credentials)
