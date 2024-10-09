import uuid
from sqlalchemy import Column, String, func, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from database.base import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID, default=uuid.uuid4, index=True, primary_key=True)
    created_at = Column(DateTime, default=func.now())


class User(BaseModel):
    __tablename__ = 'users'

    password = Column(String)
    is_active = Column(Boolean, default=False)

