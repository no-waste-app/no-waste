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
        if limit > 10:
            limit = 10

        recipesmb = mongo.db.recipes.find(limit=limit)
        all_recipes = (*recipesmb,)
        all_recipes = [z["recipe"] for z in all_recipes]
        return Recipe(many=True).load(all_recipes)
