import marshmallow as ma


class Recipe(ma.Schema):
    dish_name = ma.fields.String()
    dish_size = ma.fields.String()
    steps = ma.fields.String()
    ingredients = ma.fields.Raw()  # TODO fix nested structure type


class RecipeQueryArgsSchema(ma.Schema):
    limit = ma.fields.Integer(missing=5)
