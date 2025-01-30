from sqlalchemy import Column, Integer, ForeignKey, UUID, String
from sqlalchemy.orm import relationship

from src.db.base import Base
from src.db.models.Theme import Theme
from src.db.models.User import User


class Workbook(Base):
    __tablename__ = 'workbooks'
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String)
    theme_id = Column(UUID, ForeignKey(Theme.id))
    workbook_type = Column(Integer)
    theme =  relationship("Theme", back_populates="workbooks")
    user_id=Column(String, ForeignKey(User.id))
    user = relationship("User",back_populates="workbooks")
    materials = relationship("Material",back_populates="workbook")
