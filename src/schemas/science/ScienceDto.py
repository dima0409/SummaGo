from typing import Optional
from uuid import UUID


from pydantic import BaseModel

from src.schemas.theme.ThemeDto import ThemeDto


class ScienceDto(BaseModel):

    id: UUID
    name: str
    themes: Optional[list[ThemeDto]]
