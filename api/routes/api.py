from fastapi import APIRouter
from api.routes import test

router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(test.router)