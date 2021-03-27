import marshmallow as ma


class Ingredients(ma.Schema):
    name = ma.fields.String(required=True)
    quantity = ma.fields.String(required=True)


class Recipe(ma.Schema):
    title = ma.fields.String(required=True)
    servings = ma.fields.String()
    directions = ma.fields.String(required=True)
    ingredients = ma.fields.Nested(Ingredients, many=True, required=True)
    description = ma.fields.String(missing=None)
    imgUrl = ma.fields.String(missing=None)


class RecipeQueryArgsSchema(ma.Schema):
    limit = ma.fields.Integer(missing=10)
    offset = ma.fields.Integer(missing=0)
    short = ma.fields.Integer(missing=0)
    q = ma.fields.List(ma.fields.Str, missing=[])
