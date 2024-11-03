from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.main import get_session
from src.schemas.Transcribe import TranscribeCreateModel
from src.services.TranscribeService import TranscribeService
from src.services.UserService import UserService

transcribe_router = APIRouter()
transcribe_service = TranscribeService()
user_service = UserService()

@transcribe_router.post("/create")
async def create_transcribe(transcribe_data: TranscribeCreateModel, session: AsyncSession = Depends(get_session), authorization: Annotated[str | None, Header()] = None):
    user_id = await user_service.get_user_id(authorization)
    new_transcribe = transcribe_service.create_transcribe(transcribe_data, session, user_id)
    return new_transcribe
