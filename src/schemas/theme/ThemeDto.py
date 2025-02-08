from uuid import UUID

from pydantic import BaseModel

from src.schemas.workbook.WorkbookDto import WorkbookDto


class ThemeDto(BaseModel):
    id: UUID
    name: str
    user_id: str
    scene_id: str
    workbooks: list["WorkbookDto"]
