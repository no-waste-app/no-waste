from flask_smorest import Api

from backend.api.recipe import blp as recipe_blp
from backend.api.product import blp as product_blp


def register_api(api: Api):
    api.register_blueprint(recipe_blp)
    api.register_blueprint(product_blp)
