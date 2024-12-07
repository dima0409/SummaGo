from pydantic import BaseModel


class RegisterUserDto(BaseModel):
    name: str
    job: str
    workplace: str
