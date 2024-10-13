from datetime import datetime, timedelta
from enum import Enum

from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from typing import Annotated

SECRET_KEY = "RANDOM_GIBBERISH"  # should probably move this to env
ALGORITHM = "HS256"  # this as well
oAuth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-identity")

EXCLUDED_FROM_AUTHENTICATION = [
    '/v1/article/publish',
    '/v1/auth/update'
]


class TOKEN(Enum):
    BEARER = "Bearer"


def is_in_included_list(url_path) -> bool:
    for _path in EXCLUDED_FROM_AUTHENTICATION:
        if url_path.startswith(_path):
            return True
    return False


def create_token(user_id: str, password: str, expires_delta: timedelta) -> str:
    # TODO: Remove this when passwords will be mandatory
    encode = {'sub': password or 'hello', 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(request: Request) -> str:
    path = request.url.path
    if is_in_included_list(path):
        if not request.headers.get('Authorization'):
            return 'Authorization header is required'
        token: Annotated[str, Depends(oAuth2_scheme)] = request.headers.get('Authorization')
        identity, key = token.split()
        if key is None:
            return 'Authorization credentials were not provided.'
        if identity != TOKEN.BEARER.value:
            return 'Invalid Auth method.'
        if token:
            try:
                payload = jwt.decode(key, SECRET_KEY, algorithms=[ALGORITHM])
                password: str = payload.get('sub')
                user_email: str = payload.get('id')
                if password is None or user_email is None:
                    return 'Could not validate credentials.'
                return ''
            except JWTError as e:
                return str(e)
        return ''
    else:
        return ''
