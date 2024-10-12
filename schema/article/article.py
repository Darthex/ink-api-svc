from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

from schema.tags import TagsEnum

class ArticleBase(BaseModel):
    title: str
    content: str
    owner_id: UUID
    owner_name: str
    description: Optional[str]
    cover: Optional[str]
    tags: Optional[List[TagsEnum]] = []

class ArticleIn(ArticleBase):
    pass

class ArticleOut(ArticleBase):
    id: UUID
    created_at: datetime

class ArticlesOut(BaseModel):
    id: UUID
    created_at: datetime
    title: str
    owner_id: UUID
    owner_name: str
    description: Optional[str]
    cover: Optional[str]
    tags: Optional[List[TagsEnum]]

class HeadedArticleOut(BaseModel):
    count: int
    result: List[ArticlesOut]
