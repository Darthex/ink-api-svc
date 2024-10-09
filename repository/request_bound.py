from abc import ABC
from sqlalchemy import select, insert
from database.base import handleSession


class _BaseRepository(ABC):
    def __init__(self):
        pass

    @staticmethod
    @handleSession
    def insert_one(session, query, model):
        stmt = insert(model).values(query)  # destructure this value in parent if it's a Schema model
        result = session.execute(stmt)
        session.commit()
        (key,) = result.inserted_primary_key
        return key

    @staticmethod
    @handleSession
    def get_one(session, query, model, filters=None, single_filter=None):
        stmt = None
        if single_filter is not None:
            stmt = select(model).where(getattr(model, single_filter) == query)
        else:
            stmt = select(model).where(getattr(model, filters) == getattr(query, filters))
        result = session.execute(stmt)
        return result.scalars().one_or_none()

    @staticmethod
    @handleSession
    def get_many(session, query, model, filters=None):
        stmt = select(model).where(getattr(model, filters) == query)
        result = session.execute(stmt)
        return result.scalars().all()


class RequestBound(_BaseRepository):
    def __init__(self):
        super().__init__()
