import uuid

from pydantic import BaseModel

from src.schemas.material.MaterialDto import MaterialDto


class WorkbookDto(BaseModel):
    id: int
    theme_id: uuid.UUID

