from repository.request_bound import RequestBound


class RepositoryMixin(object):
    repo: RequestBound

    def __init__(self, repo: RequestBound):
        self.repo = repo

    def insert_one(self, *args, **kwargs):
        return self.repo.insert_one(*args, **kwargs)

    def get_one(self, *args, **kwargs):
        return self.repo.get_one(*args, **kwargs)

    def get_many(self, *args, **kwargs):
        return self.repo.get_many(*args, **kwargs)

    def get_many_paginated(self, *args, **kwargs):
        return self.repo.get_many_paginated(*args, **kwargs)

    def update_one(self, *args, **kwargs):
        return self.repo.update_one(*args, **kwargs)
