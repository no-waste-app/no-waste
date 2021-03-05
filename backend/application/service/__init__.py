import string
from json import dumps


class NoWasteService:

    def __init__(self, mongo):
        self._mongo = mongo

    def recipe_list(self, offset: int, limit: int, short: int, product):
        q = {"$and": [{"recipe.ingredients.name": v} for v in product]} if product else {}
        if short == 0:
            return self._mongo.db.recipes.find(q).skip(offset).limit(limit)
        else:
            return self._mongo.db.recipes.find(q, {"_id": 1, "recipe.title": 1}).skip(offset).limit(limit)

    # get list of products
    def products(self, query: str):
        return self._mongo.db.ingredients.find({"ingredient_name": {'$regex': query}})
