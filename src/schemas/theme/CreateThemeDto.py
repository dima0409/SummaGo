from uuid import UUID

from pydantic import BaseModel


class CreateThemeDto(BaseModel):
    name: str
    science_id: UUID

