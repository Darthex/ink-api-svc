from enum import Enum
from typing import List, Optional
from fastapi import Query
from pydantic import BaseModel

class TagsEnum(Enum):
    LIFESTYLE = 'Lifestyle'
    PROGRAMMING = 'Programming'
    TECHNOLOGY = 'Technology'
    BUSINESS = 'Business'
    ENTERTAINMENT = 'Entertainment'
    EDUCATION = 'Education'
    ENVIRONMENT = 'Environment'
    DESIGN = 'Design'
    PERSONAL = 'Personal'
    FINANCE = 'Finance'
    NEWS_POLITICS = 'News & Politics'
    SPORTS = 'Sports'

class Tags(BaseModel):
    tags: List[TagsEnum]

def tag_params(
        tags: Optional[List[TagsEnum]] = Query([], description="List of tags to filter the articles"),
):
    return Tags(tags=tags)
