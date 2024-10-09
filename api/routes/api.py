from fastapi import APIRouter
from api.routes.auth import auth

router = APIRouter(prefix="/v1", tags=["v1"])

router.include_router(auth.router)