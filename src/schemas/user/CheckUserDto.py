from pydantic import BaseModel


class CheckUserDto(BaseModel):
    id: str
    exist: bool