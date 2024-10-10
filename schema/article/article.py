from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ArticleBase(BaseModel):
    title: str
    content: str
    owner_id: UUID
    owner_name: str

class ArticleIn(ArticleBase):
    pass

class ArticleOut(ArticleBase):
    id: UUID
    created_at: datetime