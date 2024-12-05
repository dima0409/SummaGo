import os
from urllib.parse import urlparse, parse_qs
import requests
from celery import Celery

from src.services.ModelService import ModelService

c_app = Celery()

c_app.conf.broker_url =  "redis://redis:6379/0"

c_app.conf.result_backend =  "redis://redis:6379/0"
model_service = ModelService()


@c_app.task(name="start_process")
def start_process(download_link: str, user_id: str):
    download_info =  __download_video(download_link, user_id)

    file_name = download_info["file_path"]

    if download_info["is_downloaded"]:

        audio_path = f"{os.path.splitext(file_name)[0]}.mp3"

        is_mp3_created = model_service.convert_to_mp3(file_name,audio_path=audio_path)

        if is_mp3_created:
            result = model_service.get_text_from_mp3(audio_path)
            return result


def __download_video(download_link: str, save_folder: str):
    current_dir = os.getcwd()
    parsed_link = urlparse(download_link)
    file_name = parse_qs(parsed_link.query)["filename"][0]
    with requests.get(download_link, stream=True) as r:
        r.raise_for_status()
        file_path = os.path.join(current_dir, save_folder, file_name)
        user_dir_path = os.path.join(current_dir, save_folder)
        if r.status_code==200:
            if not os.path.exists(user_dir_path):
                os.makedirs(user_dir_path)
            with open(file_path, "wb") as f:
                chunk_size = 4096
                for data in r.iter_content(chunk_size):
                    f.write(data)
            return {
                "file_path": f"{file_path}",
                "is_downloaded": True
            }
        else:
            return {
                "file_path": f"{file_path}",
                "is_downloaded": False
            }
