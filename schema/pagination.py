from enum import Enum
from fastapi import Query
from pydantic import BaseModel

class SortEnum(Enum):
    ASC = "asc"
    DESC = "desc"

class Pagination(BaseModel):
    take: int
    skip: int
    sort: SortEnum
    field: str
    search: str

def pagination_params(
        skip: int = Query(ge=0, required=True, default=0),
        take: int = Query(ge=0, required=True, default=50),
        sort: SortEnum = SortEnum.DESC,
        field: str = Query(default='created_at'),
        search: str = Query(default=''),
):
    return Pagination(take=take, skip=skip, sort=sort, field=field, search=search)
