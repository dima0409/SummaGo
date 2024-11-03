import uuid
from fileinput import filename
from urllib.parse import urlparse, parse_qs

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.TranscribeModel import Transcribe
from src.routers.v1.DiskRouter import DiskService
from src.schemas.Transcribe import TranscribeCreateModel

disk_service = DiskService()

class TranscribeService:

    async def create_transcribe(self, transcribe_data: TranscribeCreateModel, session: AsyncSession, user_id: str):
        transcribe_data_dict = transcribe_data.model_dump()
        new_transcribe_data = Transcribe(**transcribe_data_dict)
        new_transcribe_data.id =uuid.uuid4().hex
        new_transcribe_data.result = ""
        new_transcribe_data.user_id = user_id
        new_transcribe_data.task_status = "Downloading"
        session.add(new_transcribe_data)
        await session.commit()
        return new_transcribe_data

    async def post_process(self,transcribe_data: TranscribeCreateModel, session: AsyncSession, user_id: str, oath_token: str):
        download_link = await disk_service.get_video_download_link(transcribe_data.file_name, oath_token)

        download_info = await self.__download_video(download_link, user_id)

        file_name = download_info["file_name"]

        if download_info["is_downloaded"]:
            print("URA")
            

    async def __download_video(self, download_link: str,save_folder: str):
        parsed_link = urlparse(download_link)

        file_name = parse_qs(parsed_link.query)["filename"][0]

        async with aiohttp.ClientSession() as session:
            async with session.get(download_link) as response:
                if response.status == 200:
                    with open(f"{save_folder}\\{file_name}", "wb") as f:
                        chunk_size = 4096
                        async for data in response.content.iter_chunked(chunk_size):
                            f.write(await data)
                            return {
                                "file_path": f"f{save_folder}\\{file_name}",
                                "is_downloaded": True
                            }
                else:
                    return {
                        "file_path": f"f{save_folder}\\{file_name}",
                        "is_downloaded": False
                    }
