from typing import Annotated

from fastapi import APIRouter, Header, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.base import get_session
from src.extension import get_current_user
from src.routers.v1.ThemeRouter import user_service
from src.schemas.user.CheckUserDto import CheckUserDto
from src.schemas.workbook.CreateWorkbookDto import CreateWorkbookDto
from src.services.UserService import UserService
from src.services.WorkbookService import WorkbookService

workbook_router = APIRouter()
workbook_service = WorkbookService()
user_service = UserService()

@workbook_router.post("/create")
async def create_workbook(new_workbook: CreateWorkbookDto,token: Annotated[str | None, Header()] = None, session: AsyncSession = Depends(get_session)):
    user = await get_current_user(token)
    user = await user_service.check_user(user,session)
    if user.exist:
        workbook = await workbook_service.create_workbook(new_workbook=new_workbook, session=session,user=user)
        return JSONResponse(jsonable_encoder(workbook), status_code=201)
    else:
        raise HTTPException(detail="User does not found in database", status_code=404)

