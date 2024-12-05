from typing import Annotated

import aiohttp
from fastapi.params import Depends
from fastapi.security import HTTPBearer

http_bearer_schema = HTTPBearer(auto_error=True)


async def decode_token(user_token: str):
    headers = {f"Authorization": f"{user_token}"}
    request_url = f"https://login.yandex.ru/info"
    status_code = 0
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(request_url, headers=headers) as response:
            status_code = response.status
    if status_code==200:
        pass

async def get_current_user(token: Annotated[str, Depends(http_bearer_schema)]):
    user = fake_decode_token(token)
    return user
