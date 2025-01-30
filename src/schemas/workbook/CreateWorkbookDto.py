import uuid

from pydantic import BaseModel


class CreateWorkbookDto(BaseModel):
    theme_id: uuid.UUID
    name: str
    workbook_type: int