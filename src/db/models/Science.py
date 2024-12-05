import uuid

from sqlalchemy import ForeignKey, Column, String, UUID
from sqlalchemy.orm import relationship

from src.db.base import Base
from src.db.models.User import User


class Science(Base):
    __tablename__ = 'sciences'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    user_id = Column(String, ForeignKey(User.id))
    user = relationship("User", back_populates="sciences")
    themes= relationship("Theme", back_populates="science")

