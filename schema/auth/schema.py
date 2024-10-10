from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UserIn(BaseModel):
    email: str
    password: str

class UserInExtended(UserIn):
    username: str

class UserOut(BaseModel):
    id: UUID
    email: str
    created_at: datetime
    is_active: bool
    username: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserOut

class UsernameUpdate(BaseModel):
    id: UUID
    username: str
