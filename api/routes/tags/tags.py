from fastapi import APIRouter
from starlette import status
from repository.tags.tags import TagsRepo
from schema.tags import Tags

router = APIRouter(prefix="/tags", tags=["tags"])

@router.get('/', status_code=status.HTTP_200_OK, response_model=Tags)
async def get_article():
    repo: TagsRepo = TagsRepo()
    response = repo.fetch_all_tags()
    return response
