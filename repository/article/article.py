from fastapi import HTTPException
from starlette import status
from models.models import Article
from repository.mixin import RepositoryMixin
from repository.request_bound import RequestBound
from schema.article.article import ArticleIn
from uuid import UUID


class ArticleRepo(RepositoryMixin, RequestBound):
    def __init__(self, repo: RequestBound = RequestBound):
        super().__init__(repo)

    def publish_article(self, article: ArticleIn):
        tags = [tags.value for tags in article.tags]
        article_dump = article.model_dump()
        article_dump['tags'] = tags
        created_id = self.insert_one(query=article_dump, model=Article)
        return created_id

    def fetch_article(self, article_id: UUID):
        model, filters = Article, 'id'
        result = self.get_one(query=article_id, model=model, single_filter=filters)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')
        return result

    def fetch_many_articles(self, pagination_params, tags):
        model = Article
        search_attributes = ['owner_name', 'title']
        count, result = (
            self.get_many_paginated(
                model=model,
                pagination_params=pagination_params,
                search_attributes=search_attributes,
                array_filter=None if not tags.tags else self.get_tags_from_enum(tags.tags),
                filter_column='tags'
            )
        )
        return {"count": count, "result": result}

    @staticmethod
    def get_tags_from_enum(tags_enum):
        return [tags.value for tags in tags_enum]
