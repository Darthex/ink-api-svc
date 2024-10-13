from fastapi import HTTPException
from starlette import status
from models.models import User
from repository.mixin import RepositoryMixin
from repository.request_bound import RequestBound
from schema.auth.schema import UserIn, UsernameUpdate
from datetime import timedelta
from utils.tokens import create_token

class Auth(RepositoryMixin, RequestBound):
    def __init__(self, repo: RequestBound = RequestBound):
        super().__init__(repo)

    def create_user(self, user_details: UserIn):
        existing_user = self.find_user(user_details, creating_user = True)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User already exists')
        created_id = self.insert_one(query=user_details.model_dump(), model=User)
        return created_id

    def find_user(self, user_details: UserIn, creating_user = False, default_filter = 'email'):
        model, filters = User, default_filter
        user = self.get_one(query=user_details, model=model, filters=filters)
        print(not user and not creating_user)
        if not user and not creating_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        return user

    def update_user(self, user: UsernameUpdate):
        model = User
        user_id = user.id
        existing_user = self.find_user(user, default_filter = 'id')
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_FORBIDDEN, detail='User not found')
        response = self.update_one(model=model, record_id=user_id, update_values=user.model_dump())
        return response

    def login_user(self, user: UserIn):
        model, filters = User, 'email'

        def authenticate():
            existing_user = self.find_user(user)
            print(existing_user.password, user.password)
            if not existing_user:
                return False
            if existing_user.password != user.password:
                return False
            # if not bcrypt_context.verify(user.password, existing_user.password):
            #     return False
            return existing_user

        returned_user = authenticate()
        if not returned_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Could not validate credentials')
        token = create_token(returned_user.email, returned_user.password, timedelta(minutes=30))

        return {
            'access_token': token,
            'token_type': 'bearer',
            'user': returned_user
        }
