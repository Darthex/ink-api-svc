from fastapi import APIRouter
from starlette import status
from repository.article.article import ArticleRepo
from schema.article.article import ArticleIn, ArticleOut
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
