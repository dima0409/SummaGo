import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.Theme import Theme
from src.db.models.Workbook import Workbook
from src.schemas.theme.CreateThemeDto import CreateThemeDto
from src.schemas.theme.ThemeDto import ThemeDto
from src.schemas.user.CheckUserDto import CheckUserDto


class ThemeService():
    async def create_theme(self, user: CheckUserDto, new_theme: CreateThemeDto, session: AsyncSession):
        new_theme.name =new_theme.name.strip()
        new_theme.name = ' '.join(new_theme.name.split())
        theme_id = uuid.uuid4()
        new_theme = Theme(user_id=user.id, name=new_theme.name, science_id=new_theme.science_id, id=theme_id)
        session.add(new_theme)
        await session.commit()
        return  new_theme

    async def get_all_workbooks(self, theme_id: uuid.UUID, session: AsyncSession):
        workbooks = await session.execute(select(Workbook).where(Workbook.theme_id == theme_id))
        workbooks = workbooks.scalars().all()
        return workbooks
