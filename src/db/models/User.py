import uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship

from src.db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name =  Column(String)
    job = Column(String)

    email = Column(String)
    login = Column(String)
    workplace = Column(String)
    sciences = relationship("Science",back_populates = "user")
    materials = relationship("Material",back_populates = "user")
    workbooks = relationship("Workbook",back_populates = "user")
    themes = relationship("Theme",back_populates = "user")
