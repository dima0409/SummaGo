from typing import Annotated

from fastapi import APIRouter, UploadFile, Depends, Body
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db.base import get_session
from src.extension import get_current_user
from src.schemas.material.CreateMaterialFile import CreateMaterialFileDto
from src.services.MaterialService import MaterialService
from src.services.UserService import UserService

material_router = APIRouter()
user_service = UserService()
security = HTTPBearer()
material_service = MaterialService()


@material_router.post("/create")
async def create_material(
    file: UploadFile,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    new_material: CreateMaterialFileDto = Body(...),
    session: AsyncSession = Depends(get_session),
):

    user = await get_current_user(credentials.credentials)
    user = await user_service.check_user(user, session)
    if user.exist:
        material = await material_service.create_file_material(
            user=user, session=session, new_material=new_material, material_file=file
        )
        return JSONResponse(jsonable_encoder(material), status_code=201)
