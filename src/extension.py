import aiohttp
from fastapi import HTTPException
from fastapi.security import HTTPBearer

from src.schemas.user.CheckUserDto import CheckUserDto
from src.services.UserService import UserService

http_bearer_schema = HTTPBearer(auto_error=True)
user_service = UserService()

async def get_current_user(token: str):

    headers = {f"Authorization": f"{token}"}
    request_url = f"https://login.yandex.ru/info"

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(request_url, headers=headers) as response:
            status_code = response.status
            print(response)
            if status_code==200:
                data = await response.json()
                user = CheckUserDto(id=data["id"],exist=False)
                return user
            else:
                raise HTTPException(detail="User token is not valid",status_code=401)
