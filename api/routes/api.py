from fastapi import APIRouter
from api.routes.auth import auth
from api.routes.article import article
from api.routes.tags import tags

router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(auth.router)
router.include_router(article.router)
router.include_router(tags.router)
