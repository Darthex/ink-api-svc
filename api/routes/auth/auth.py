from fastapi import APIRouter
from starlette import status
from repository.auth.auth import Auth
from schema.auth.schema import UserIn, LoginResponse, UserInExtended, UsernameUpdate

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: UserInExtended):
    repo: Auth = Auth()
    response = repo.create_user(request)
    return { 'User created' : response }

@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
async def login(request: UserIn):
    repo: Auth = Auth()
    response = repo.login_user(request)
    return response

@router.post('/update', status_code=status.HTTP_200_OK)
async def update(request: UsernameUpdate):
    repo: Auth = Auth()
    response = repo.update_user(request)
    return { 'User updated' : response }
