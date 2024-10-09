from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UserIn(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: UUID
    email: str
    created_at: datetime
    is_active: bool


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
