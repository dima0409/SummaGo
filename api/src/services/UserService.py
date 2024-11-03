import aiohttp


class UserService:
    URL: str
    def __init__(self) -> None:
        self.URL =  "https://login.yandex.ru"

    async def get_user_id(self,oauth_token: str):

        async with aiohttp.ClientSession() as session:
            request_url = f"{self.URL}/info?oauth_token={oauth_token}"
            async with session.get(request_url) as response:
                if response.ok:
                    result = await response.json()
                    return result["id"]
