from fastapi import HTTPException
from starlette import status
from models.models import User
from repository.mixin import RepositoryMixin
from repository.request_bound import RequestBound
from schema.auth.schema import UserIn


class Auth(RepositoryMixin, RequestBound):
    def __init__(self, repo: RequestBound = RequestBound):
        super().__init__(repo)

    def create_user(self, user_details: UserIn):
        existing_user = self.find_user(user_details, creating_user = True)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='User already exists')
        created_id = self.insert_one(query=user_details.model_dump(), model=User)
        return created_id

    def find_user(self, user_details: UserIn, creating_user = False):
        model, filters = User, 'email'
        user = self.get_one(query=user_details, model=model, filters=filters)
        print(not user and not creating_user)
        if not user and not creating_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        return user
