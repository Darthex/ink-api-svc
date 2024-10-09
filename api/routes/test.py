from fastapi import APIRouter
from starlette import status

router = APIRouter(prefix="/test", tags=["test"])

@router.get("/status", status_code=status.HTTP_200_OK)
async def status():
    return { 'status': 'okay' }
