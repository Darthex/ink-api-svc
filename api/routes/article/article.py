from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status
from repository.article.article import ArticleRepo
from schema.pagination import Pagination, pagination_params
from schema.tags import Tags, tag_params
from schema.article.article import ArticleIn, ArticleOut, HeadedArticleOut
from uuid import UUID

router = APIRouter(prefix="/article", tags=["article"])

@router.post('/publish', status_code=status.HTTP_201_CREATED)
async def publish(article: ArticleIn):
    repo: ArticleRepo = ArticleRepo()
    response = repo.publish_article(article)
    return response

@router.get('/{article_id}', status_code=status.HTTP_200_OK, response_model=ArticleOut)
async def get_article(article_id: UUID):
    repo: ArticleRepo = ArticleRepo()
    response = repo.fetch_article(article_id)
    return response

@router.get('/', response_model=HeadedArticleOut)
async def get_articles(
        pagination: Annotated[Pagination, Depends(pagination_params)],
        tags: Annotated[Tags, Depends(tag_params)],
):
    repo: ArticleRepo = ArticleRepo()
    response = repo.fetch_many_articles(pagination, tags)
    return response
