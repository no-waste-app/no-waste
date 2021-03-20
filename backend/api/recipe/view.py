from flask.views import MethodView
from flask_smorest import Blueprint
from backend.api.recipe.models import RecipeQueryArgsSchema, Recipe
from backend.core.db import mongo

blp = Blueprint(
    "recipes", "recipes", url_prefix="/api/recipes", description="Operations on recipes"
)


@blp.route("/")
class Recipes(MethodView):
    @blp.arguments(RecipeQueryArgsSchema, location="query")
    @blp.response(200, Recipe(many=True))
    def get(self, args: RecipeQueryArgsSchema):
        """List recipes"""
        limit = args["limit"]
        offset = args["offset"]
        short = args["short"]
        product = args["q"]
        q = {"$and": [{"recipe.ingredients.name": v} for v in product]} if product else {}

        if short:
            recipesmb = mongo.db.recipes.find(q, {"_id": 1, "recipe.title": 1}, limit=limit, skip=offset)
        else:
            recipesmb = mongo.db.recipes.find(q, limit=limit, skip=offset)
        all_recipes = (*recipesmb,)
        all_recipes = [z["recipe"] for z in all_recipes]
        return Recipe(many=True).load(all_recipes)
