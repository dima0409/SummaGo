from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends, Query
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.base import get_session
from src.schemas.material.CreateMaterialUrlDto import CreateMaterialUrlDto
from src.schemas.material.MaterialDto import MaterialDto
from src.services.TranscribeService import TranscribeService
from src.services.UserService import UserService

transcribe_router = APIRouter()
transcribe_service = TranscribeService()
user_service = UserService()

security = HTTPBearer(auto_error=True)


@transcribe_router.post("/create",
                        response_model=MaterialDto,
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
async def create_transcribe( user: Annotated[str, Depends(security)],transcribe_data: CreateMaterialUrlDto, session: AsyncSession = Depends(get_session)):
    new_transcribe = await transcribe_service.create_transcribe(transcribe_data, session, oauth_token=user)
    return new_transcribe

@transcribe_router.get("/get",)
async def get_transcribe(transcribe_id: Annotated[str | None, Query()] = None, user_id: Annotated[str | None, Query()] = None, session: AsyncSession = Depends(get_session)):
    return await transcribe_service.get_transcribe(user_id=user_id, session=session,transcribe_id=transcribe_id)