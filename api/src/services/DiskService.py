import aiohttp


class DiskService:
    URL: str
    def __init__(self) -> None:
        self.URL =  "https://cloud-api.yandex.net/v1/disk"

    async def get_user_video(self, user_token: str):
        headers = {f"Authorization": f"{user_token}"}
        request_url = f"{self.URL}/resources/files?media_type=video&fields=name,file,size"
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(request_url, headers=headers) as response:
                return await response.json()

    async def get_video_download_link(self, user_token: str, video_path: str):
        headers = {f"Authorization": f"{user_token}"}
        request_url = f"{self.URL}/resources/download?path={video_path}"
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(request_url, headers=headers) as response:
                return await response.json()["href"]