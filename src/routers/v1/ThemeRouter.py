import uuid
from typing import Annotated

from fastapi import APIRouter, Header, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.base import get_session
from src.extension import get_current_user
from src.schemas.theme.CreateThemeDto import CreateThemeDto
from src.services.ScienceService import user_service
from src.services.ThemeService import ThemeService
from src.services.UserService import UserService

theme_router = APIRouter()
theme_service = ThemeService()
user_service =  UserService()
@theme_router.post("/create")
async def create_theme(new_theme: CreateThemeDto,token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    user = await get_current_user(token)
    user = await user_service.check_user(user,session)
    if user.exist:
        theme = await theme_service.create_theme(user,new_theme, session)
        return JSONResponse(jsonable_encoder(theme),status_code=201)
    else:
        raise HTTPException(detail="User does not found in database", status_code=404)
@theme_router.get("/get_workbooks")
async def get_all_workbooks(theme_id: uuid.UUID, token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    try:
        user = await get_current_user(token)
        user = await user_service.check_user(user,session)
        if user.exist:
            workbooks = await theme_service.get_all_workbooks(theme_id, session)
            if len(workbooks) == 0:
                raise HTTPException(detail="No sciences found", status_code=404)
            else:
                return workbooks
        else:
            raise HTTPException(detail="User does not found in database", status_code=404)
    except HTTPException as e:
        return JSONResponse(content=e.detail,status_code=e.status_code)
    except Exception as e:
        return JSONResponse(content=e.args, status_code=400)