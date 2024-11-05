from typing import Annotated

from certifi import contents
from fastapi import APIRouter, BackgroundTasks
from fastapi.params import Header, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.main import get_session
from src.schemas.Transcribe import TranscribeCreateModel, TranscribeModel
from src.services.TranscribeService import TranscribeService
from src.services.UserService import UserService

transcribe_router = APIRouter()
transcribe_service = TranscribeService()
user_service = UserService()

@transcribe_router.post("/create",
                        response_model=TranscribeModel,
                        responses={
                            200:{
                                "description": "Successful created task",
                                "content": {
                                    "application/json": {
                                    }
                                }
                            },
                        }
                        )
async def create_transcribe(transcribe_data: TranscribeCreateModel, session: AsyncSession = Depends(get_session), token: Annotated[str | None, Header()] = None):
    new_transcribe = await transcribe_service.create_transcribe(transcribe_data, session, oauth_token=token)
    return new_transcribe

@transcribe_router.get("/get",)
async def get_transcribe(transcribe_id: Annotated[str | None, Query()] = None, user_id: Annotated[str | None, Query()] = None, session: AsyncSession = Depends(get_session)):
    return await transcribe_service.get_transcribe(user_id=user_id, session=session,transcribe_id=transcribe_id)