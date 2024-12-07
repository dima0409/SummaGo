from pydantic import BaseModel


class UserDto(BaseModel):

    id: str
    name: str
    job: str
    workplace: str

