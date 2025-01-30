import uuid

from pydantic import BaseModel

from src.schemas.material.MaterialDto import MaterialDto


class WorkbookDto(BaseModel):
    id: int
    workbook_type: int
    name: str
    theme_id: uuid.UUID
