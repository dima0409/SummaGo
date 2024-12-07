import uuid

from sqlalchemy import Column, Integer, ForeignKey, String, UUID
from sqlalchemy.orm import relationship

from src.db.base import Base
from src.db.models.Theme import Theme
from src.db.models.User import User
from src.db.models.Workbook import Workbook


class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String)
    url = Column(String)
    name = Column(String)
    status  = Column(String)
    result = Column(String)
    user = relationship("User", back_populates="materials")
    user_id  = Column(String, ForeignKey(User.id))
    workbook_id = Column(Integer, ForeignKey(Workbook.id))
    workbook = relationship("Workbook", back_populates="materials")
    theme_id = Column(UUID, ForeignKey(Theme.id))
    