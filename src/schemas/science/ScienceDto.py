from uuid import UUID

from pydantic import BaseModel
from pydantic.v1 import UUID1


class ScienceDto(BaseModel):

    id: UUID
    name: str