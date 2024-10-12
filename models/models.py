import uuid
from sqlalchemy import Column, String, func, DateTime, Boolean, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from database.base import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID, default=uuid.uuid4, index=True, primary_key=True)
    created_at = Column(DateTime, default=func.now())

class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    username = Column(String, nullable=False)
    tags = Column(ARRAY(String), default=[])

class Article(BaseModel):
    __tablename__ = 'articles'

    owner_id = Column(String, nullable=False, index=True)
    owner_name = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    description = Column(String)
    cover = Column(String)
    tags = Column(ARRAY(String), default=[])