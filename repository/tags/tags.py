from schema.tags import TagsEnum

class TagsRepo:
    def __init__(self):
        pass

    @staticmethod
    def fetch_all_tags():
        return { "tags" : [each.value for each in TagsEnum] }

