import uuid

from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from celery.result import AsyncResult

from src.db.models.TranscribeModel import Transcribe
from src.routers.v1.DiskRouter import disk_service
from src.schemas.Transcribe import TranscribeCreateModel, TranscribeUpdateModel
from src.services.celery import start_process
from src.services.DiskService import DiskService
from src.services.UserService import UserService

disk_service = DiskService()
user_service = UserService()

class TranscribeService:

    async def create_transcribe(self, transcribe_data: TranscribeCreateModel, session: AsyncSession, oauth_token: str):

        video_download_link = await disk_service.get_video_download_link(user_token=oauth_token,video_path=transcribe_data.file_name)

        user_id = await user_service.get_user_id(oauth_token=oauth_token)

        transcribe_data_dict = transcribe_data.model_dump()

        task = start_process.delay(video_download_link, user_id)

        new_transcribe_data = Transcribe(**transcribe_data_dict)

        new_transcribe_data.id =task.id

        new_transcribe_data.result = ""
        new_transcribe_data.user_id = user_id
        new_transcribe_data.task_status = "Processing"
        session.add(new_transcribe_data)




        start_process.delay(video_download_link, user_id)
        await session.commit()
        return new_transcribe_data

    async def get_transcribe(self, transcribe_id: str, user_id: str, session: AsyncSession):

        transcribe_result = AsyncResult(transcribe_id)
        if transcribe_result.state == "PENDING":
            return await session.get(Transcribe, transcribe_id)

        if transcribe_result.state == "SUCCESS":
            stm = update(Transcribe).where(Transcribe.id == transcribe_id).values({Transcribe.result: transcribe_result.result, Transcribe.task_status: "Completed"})
            await session.execute(stm)
        await session.commit()

        return await session.get(Transcribe, transcribe_id)