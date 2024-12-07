import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.Science import Science
from src.db.models.Theme import Theme
from src.schemas.science.CreateScienceDto import CreateScienceDto
from src.schemas.science.ScienceDto import ScienceDto
from src.schemas.theme.ThemeDto import ThemeDto
from src.schemas.user.CheckUserDto import CheckUserDto
from src.services.UserService import UserService

user_service = UserService()
class ScienceService():

    async def create_science(self, user: CheckUserDto, new_science: CreateScienceDto, session:AsyncSession):

        science_name=new_science.name.strip()
        science_name = ' '.join(science_name.split())
        exist_science = await session.execute(select(Science).where(Science.name==science_name and Science.user_id==user.id))
        if exist_science.first() is not None:
            raise Exception("Science with same name is already exists")
        science_id = uuid.uuid4()
        new_science = Science(id=science_id,name=science_name,user_id=user.id)
        session.add(new_science)
        await session.commit()

        return ScienceDto(name=science_name, id=science_id, themes=[])


    async def get_all_sciences(self, user: CheckUserDto, session:AsyncSession):
        sciences = await session.execute(select(Science).where(Science.user_id==user.id))
        sciences = sciences.scalars().all()
        return sciences

    async def get_themes_for_science(self, science_id: uuid.UUID, session: AsyncSession):
        themes = await session.execute(select(Theme).where(Theme.science_id==science_id))
        themes = themes.scalars().all()
        return themes

