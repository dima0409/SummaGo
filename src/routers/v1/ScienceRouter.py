
from typing import Annotated

from fastapi import APIRouter, Header, Depends,HTTPException
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
            return await science_services.create_science(user,new_science, session)
        else:
            raise HTTPException(detail="User does not found in database", status_code=404)

    except HTTPException as e:
        return JSONResponse(content=f"{e.detail}", status_code=404)
    except Exception as e:
        return JSONResponse(content=f"{e.args}", status_code=500)
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


