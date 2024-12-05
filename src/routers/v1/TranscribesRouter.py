from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends, Query, Header
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.base import get_session
from src.extension import get_current_user
from src.schemas.material.CreateMaterialUrlDto import CreateMaterialUrlDto
from src.schemas.material.MaterialDto import MaterialDto
from src.schemas.user.UserDto import UserDto
from src.services.TranscribeService import TranscribeService
from src.services.UserService import UserService

transcribe_router = APIRouter()
transcribe_service = TranscribeService()
user_service = UserService()




@transcribe_router.post("/create",
                        )
async def create_transcribe( token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    user =await get_current_user(token)
    return user


@transcribe_router.get("/get",)
async def get_transcribe(transcribe_id: Annotated[str | None, Query()] = None, user_id: Annotated[str | None, Query()] = None, session: AsyncSession = Depends(get_session)):
    return await transcribe_service.get_transcribe(user_id=user_id, session=session,transcribe_id=transcribe_id)