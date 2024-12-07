from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.User import User
from src.schemas.user.CheckUserDto import CheckUserDto
from src.schemas.user.RegisterUserDto import RegisterUserDto
from src.schemas.user.UserDto import UserDto


class UserService:
    URL: str
    def __init__(self) -> None:
        self.URL =  "https://login.yandex.ru"

    async def check_user(self, user: CheckUserDto, session: AsyncSession):
        exist_user = await session.execute(select(User).where(User.id==user.id))
        res = CheckUserDto(id=user.id, exist=False)

        if exist_user.first() is not None:

            res.exist = True
        else:
            res.exist = False
        return res
    async def register_user(self,ya_user: CheckUserDto,new_user: RegisterUserDto, session: AsyncSession):
        user = await session.execute(select(User).where(User.id==ya_user.id))

        if user.first() is not None:
            raise Exception("User is exists")
        user = User(job=new_user.job, id=ya_user.id, workplace=new_user.workplace, name=new_user.name)

        session.add(user)
        await session.commit()
        return UserDto(name=user.name, id=user.id, job=user.job, workplace=user.workplace)

