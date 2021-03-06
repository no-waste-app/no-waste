from flask import Flask
from flask.views import MethodView
from flask_pymongo import PyMongo
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort

app = Flask(__name__)
app.config.from_object("config.config.ProductionConfig")

mongo = PyMongo(app)
api = Api(app)

blp = Blueprint(
    "recipes", "recipes", url_prefix="/api/recipes", description="Operations on recipes"
)


class Recipe(ma.Schema):
    dish_name = ma.fields.String()
    dish_size = ma.fields.String()
    steps = ma.fields.String()
    ingredients = ma.fields.Raw()


class RecipeQueryArgsSchema(ma.Schema):
    limit = ma.fields.Integer(missing=5)


@blp.route("/")
class Recipes(MethodView):
    @blp.arguments(RecipeQueryArgsSchema, location="query")
    @blp.response(200, Recipe(many=True))
    def get(self, args: RecipeQueryArgsSchema):
        """List pets"""
        limit = args["limit"]
        if limit > 10:
            limit = 10

        recipesmb = mongo.db.recipes.find(limit=limit)
        a = (*recipesmb,)
        a = [z["recipe"] for z in a]
        x = Recipe(many=True).load(a)
        return x

    # @blp.arguments(PetSchema)
    # @blp.response(201, PetSchema)
    # def post(self, new_data):
    #     """Add a new pet"""
    #     item = Pet.create(**new_data)
    #     return item


rlp = Blueprint(
    "products",
    "products",
    url_prefix="/api/products",
    description="Operations on products",
)


class ProductQueryArgs(ma.Schema):
    q = ma.fields.String(required=True)


class Product(ma.Schema):
    ingredient_name = ma.fields.String(required=True)


@rlp.route("/")
class Products(MethodView):
    @rlp.arguments(ProductQueryArgs, location="query")
    @rlp.response(200, Product(many=True))
    def get(self, args: ProductQueryArgs):
        ingredient = args["q"].lower()
        print(ingredient)
        ingredientsmb = mongo.db.ingredients.find(
            {"ingredient_name": {"$regex": ingredient}}
        )

        a = (*ingredientsmb,)
        z = Product(many=True, unknown=ma.EXCLUDE).load(a)
        return z


api.register_blueprint(blp)
api.register_blueprint(rlp)


def main():
    app.run(port=8080)


if __name__ == "__main__":
    main()
