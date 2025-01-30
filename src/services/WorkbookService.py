from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.Workbook import Workbook
from src.schemas.user.CheckUserDto import CheckUserDto
from src.schemas.workbook.CreateWorkbookDto import CreateWorkbookDto


class WorkbookService:
    async def create_workbook(self, new_workbook: CreateWorkbookDto, session: AsyncSession,user: CheckUserDto):
        new_workbook.name = new_workbook.name.strip()
        new_workbook.name = ' '.join(new_workbook.name.split())
        workbook = Workbook(theme_id=new_workbook.theme_id, name=new_workbook.name, user_id=user.id,workbook_type=new_workbook.workbook_type)
        session.add(workbook)
        await session.commit()
        return new_workbook

