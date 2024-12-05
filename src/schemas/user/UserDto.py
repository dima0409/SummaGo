from pydantic import BaseModel


class UserDto(BaseModel):
    login: str
    id: str
    name: str
    email: str
    job: str
    workplace: str

