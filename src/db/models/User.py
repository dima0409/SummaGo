import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from src.db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name =  Column(String)
    job = Column(String)
    workplace = Column(String)
    sciences = relationship("Science",back_populates = "user")
    materials = relationship("Material",back_populates = "user")
    workbooks = relationship("Workbook",back_populates = "user")
    themes = relationship("Theme",back_populates = "user")
