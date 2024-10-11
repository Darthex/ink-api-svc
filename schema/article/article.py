from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ArticleBase(BaseModel):
    title: str
    content: str
    owner_id: UUID
    owner_name: str
    description: Optional[str]
    cover: Optional[str]

class ArticleIn(ArticleBase):
    pass

class ArticleOut(ArticleBase):
    id: UUID
    created_at: datetime

class HeadedArticleOut(BaseModel):
    count: int
    result: List[ArticleOut]
