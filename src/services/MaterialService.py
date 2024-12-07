from uuid import uuid4

import aiofiles
from celery.bin.result import result
from requests import session
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.Material import Material
from src.schemas.material.CreateMaterialFile import CreateMaterialFileDto
from src.schemas.material.MaterialDto import MaterialDto
from src.schemas.user.CheckUserDto import CheckUserDto


class MaterialService():
    async def create_file_material(self, user: CheckUserDto, new_material: CreateMaterialFileDto, session: AsyncSession):
        path_helper = uuid4()
        async with aiofiles.open(f"\\files\\{path_helper}\\{new_material.file.filename}", 'wb') as out_file:
            content = await new_material.read()
            await out_file.write(content)
        material = Material(user_id=user.id, name=new_material.file.filename, path=f"\\files\\{path_helper}\\{new_material.file.filename}", workbook_id=new_material.workbook_id, theme_id=new_material.theme_id, url=f"\\files\\{path_helper}\\{new_material.file.filename}",result="", status="PROCESSING")
        session.add(material)
        await session.commit()
        return MaterialDto(name=material.name, workbook_id=material.workbook_id, status=material.status, result="", url=f"\\files\\{path_helper}\\{new_material.file.filename}",)