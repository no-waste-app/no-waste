import marshmallow as ma


class ProductQueryArgs(ma.Schema):
    q = ma.fields.String(required=True)


class Product(ma.Schema):
    name = ma.fields.String(required=True)
