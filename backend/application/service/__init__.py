from json import dumps


class NoWasteService:

    def __init__(self, mongo):
        self._mongo = mongo

    def recipe_list(self):
        return self._mongo.db.recipes.find()

    # get list of products
    def products(self, query: str):
        return self._mongo.db.ingredients.find({"ingredient_name": {'$regex': query}})
