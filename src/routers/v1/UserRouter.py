
from typing import Annotated

from fastapi import APIRouter, Header, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.base import get_session
from src.extension import get_current_user
from src.schemas.user.RegisterUserDto import RegisterUserDto
from src.services.UserService import UserService

user_router = APIRouter()
user_service = UserService()

@user_router.post("/check")
async def check_user(token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    user = await get_current_user(token)
    return await user_service.check_user(user,session)
@user_router.post("/register")
async def register_user(new_user: RegisterUserDto, token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    try:
        user = await get_current_user(token)
        if user is not None and new_user.id==user.id:
            res = await user_service.register_user(new_user, session)
            return JSONResponse(content=res.json(),status_code=201)
        raise HTTPException(detail={"message":"Unauthorized" },status_code=401)
    except HTTPException as e:
        return JSONResponse(content=e.detail, status_code=401)
    except Exception as e:
        return JSONResponse(content=e.args, status_code=500)