import uuid

from sqlalchemy import Column
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.orm import declarative_base
from sqlmodel import SQLModel


Base = declarative_base()
class Transcribe(SQLModel, table=True, Base):
    __tablename__ = 'statuses'
    id: uuid.UUID =Column(pg.UUID,nullable = False, primary_key = True, default=uuid.uuid4)
    user_id: uuid.UUID = Column(pg.UUID, nullable = False)
    file_name: str
    task_status: str
    result: str
