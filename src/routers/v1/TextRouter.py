from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.base import get_session
from src.services.Text.model import TextModelService

text_router = APIRouter()
text_service = TextModelService()
@text_router.get("/summarize")
async def summarize(transcribe_data: str, session: AsyncSession = Depends(get_session)):
    new_transcribe = await text_service.create_transcribe(transcribe_data, session, oauth_token=token)
    return new_transcribe
