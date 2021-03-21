from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Blueprint, abort

from backend.api.product.models import ProductQueryArgs, Product
from backend.core.db import mongo

blp = Blueprint(
    "products",
    "products",
    url_prefix="/api/products",
    description="Operations on products",
)


@blp.route("/")
class Products(MethodView):
    @blp.arguments(ProductQueryArgs, location="query")
    @blp.response(200, Product(many=True))
    def get(self, args: ProductQueryArgs):
        ingredient = args["q"].lower()

        ingredientsmb = mongo.db.ingredients.find(
             {"name": {"$regex": ingredient}}
        )

        all_ingredients = (*ingredientsmb,)
        return Product(many=True, unknown=ma.EXCLUDE).load(all_ingredients)
