from abc import ABC
from sqlalchemy import insert, select, update, desc, asc, func, or_
from database.base import handleSession
from schema.pagination import SortEnum

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

    @staticmethod
    @handleSession
    def get_many_paginated(session, model, pagination_params, search_attributes, array_filter: list[str] = None, filter_column = ''):
        select_stmt = select(model)
        if array_filter:
            select_stmt = select_stmt.filter(
                or_(*(getattr(model, filter_column).any(tag) for tag in array_filter))
            )
        order = desc if pagination_params.sort == SortEnum.DESC else asc
        stmt = (select_stmt
                .limit(pagination_params.take)
                .offset(pagination_params.skip)
                .order_by(order(getattr(model, pagination_params.field))))
        search_conditions = []
        if pagination_params.search != '':
            for attr in search_attributes:
                column_attr = getattr(model, attr)
                search_conditions.append(column_attr.ilike(f'%{pagination_params.search}%'))
        if search_conditions:
            stmt = stmt.where(or_(*search_conditions))
        result = session.execute(stmt).scalars().all()
        count_stmt = select(func.count()).select_from(model)
        if array_filter:
            count_stmt = count_stmt.where(
                or_(*(getattr(model, filter_column).any(tag) for tag in array_filter))
            )
        if search_conditions:
            count_stmt = count_stmt.where(or_(*search_conditions))
        count = session.execute(count_stmt).scalar_one()
        return count, result

    @staticmethod
    @handleSession
    def update_one(session, record_id, update_values, model):
        stmt = update(model).where(getattr(model, 'id') == record_id).values(update_values)
        result = session.execute(stmt)
        session.commit()
        return True


class RequestBound(_BaseRepository):
    def __init__(self):
        super().__init__()
