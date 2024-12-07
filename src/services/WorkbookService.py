from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.user.CheckUserDto import CheckUserDto
from src.schemas.workbook.CreateWorkbookDto import CreateWorkbookDto


class WorkbookService:
    async def create_workbook(self, new_workbook: CreateWorkbookDto, session: AsyncSession):
        new_workbook.name = new_workbook.name.strip()
        new_workbook.name = ' '.join(new_workbook.name.split())
        session.add(new_workbook)
        await session.commit()
        return new_workbook

