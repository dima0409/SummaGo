
from typing import Annotated

from fastapi import APIRouter, Header, Depends,HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.base import get_session
from src.extension import get_current_user
from src.schemas.user.RegisterUserDto import RegisterUserDto
from src.services.UserService import UserService

user_router = APIRouter()
user_service = UserService()
security = HTTPBearer()

@user_router.post("/check")
async def check_user(  credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)], session: AsyncSession = Depends(get_session)):
    user = await get_current_user(credentials.credentials)
    return await user_service.check_user(user,session)
@user_router.post("/register")
async def register_user(new_user: RegisterUserDto,   credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)], session: AsyncSession = Depends(get_session)):
    try:
        user = await get_current_user(credentials.credentials)
        if user is not None:

            res = await user_service.register_user(new_user=new_user, session=session, ya_user=user)

            return JSONResponse(content=res.model_dump(), status_code=201)
        raise HTTPException(detail={"message":"Unauthorized" },status_code=401)
    except HTTPException as e:
        return JSONResponse(content=e.detail, status_code=401)



