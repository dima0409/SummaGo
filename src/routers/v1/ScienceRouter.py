import uuid
from typing import Annotated

from fastapi import APIRouter, Header, Depends,HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.base import get_session
from src.extension import get_current_user
from src.schemas.science.CreateScienceDto import CreateScienceDto
from src.services.ScienceService import ScienceService
from src.services.UserService import UserService

science_router = APIRouter()
science_services = ScienceService()
user_service = UserService()
@science_router.post("/create")
async def create_science(new_science: CreateScienceDto,token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    try:
        user = await get_current_user(token)
        user = await user_service.check_user(user,session)
        if user.exist:
            science = await science_services.create_science(user,new_science, session)
            return JSONResponse(jsonable_encoder(science), 201)
        else:
            raise HTTPException(detail="User does not found in database", status_code=404)

    except HTTPException as e:
        return JSONResponse(content=f"{e.detail}", status_code=404)

@science_router.get("/get_all")
async def get_all_sciences(token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    try:
        user = await get_current_user(token)
        user = await user_service.check_user(user,session)
        if user.exist:
            sciences = await science_services.get_all_sciences(user,session)
            if len(sciences) == 0:
                raise HTTPException(detail="No sciences found", status_code=404)
            else:
                return sciences
        else:
            raise HTTPException(detail="User does not found in database", status_code=404)
    except HTTPException as e:
        return JSONResponse(content=e.detail,status_code=e.status_code)
    except Exception as e:
        return JSONResponse(content=e.args, status_code=400)
@science_router.get("/get_themes")
async def get_themes(science_id: uuid.UUID, token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    try:
        user = await get_current_user(token)
        user = await user_service.check_user(user,session)
        if user.exist:
            themes = await science_services.get_themes_for_science(science_id, session)
            if len(themes) == 0:
                raise HTTPException(detail="No themes found for current science", status_code=404)
            else:
                return themes
        else:
            raise HTTPException(detail="User does not found in database", status_code=404)
    except HTTPException as e:
        return JSONResponse(content=e.detail,status_code=e.status_code)
