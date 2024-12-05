from pydantic import BaseModel


class CreateScienceDto(BaseModel):
    name: str

