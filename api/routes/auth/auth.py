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
    response = repo.find_user(request)
    return { 'user': response, 'access_token': 'abcd_test_okay', 'token_type': 'bearer' }

@router.post('/update', status_code=status.HTTP_200_OK)
async def update(request: UsernameUpdate):
    repo: Auth = Auth()
    response = repo.update_user(request)
    return { 'User updated' : response }
