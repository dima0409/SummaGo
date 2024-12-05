from pydantic import BaseModel


class RegisterUserDto(BaseModel):
    name: str
    email: str
    id: str
    job: str
    workplace: str
    login: str