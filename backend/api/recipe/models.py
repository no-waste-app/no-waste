import marshmallow as ma


class Recipe(ma.Schema):
    title = ma.fields.String()
    servings = ma.fields.String()
    directions = ma.fields.String()
    ingredients = ma.fields.Raw()  # TODO fix nested structure type
    description = ma.fields.String(missing=None)
    imgUrl = ma.fields.String(missing=None)


class RecipeQueryArgsSchema(ma.Schema):
    limit = ma.fields.Integer(missing=10)
    offset = ma.fields.Integer(missing=0)
    short = ma.fields.Integer(missing=0)
    q = ma.fields.List(ma.fields.Str, missing=[])
