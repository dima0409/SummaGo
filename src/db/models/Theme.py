import uuid

from sqlalchemy import Column, String, ForeignKey, UUID
from sqlalchemy.orm import relationship

from src.db.base import Base
from src.db.models.Science import Science
from src.db.models.User import User


class Theme(Base):
    __tablename__ = 'themes'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    user_id =  Column(UUID, ForeignKey(User.id))
    user = relationship("User",back_populates="themes")
    workbooks = relationship("Workbook",back_populates="theme")
    science_id = Column(UUID, ForeignKey(Science.id))
    science = relationship("Science", back_populates="themes")

