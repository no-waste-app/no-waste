import os
import string

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps, loads
from application.service import NoWasteService

# main Flask module
app = Flask(__name__)
app.config.from_object("config.config.ProductionConfig")

service: NoWasteService


# all recipes in database
@app.route("/recipes")
def recipelist():
    offset = request.args.get("offset", 0, type=int)
    limit = request.args.get("limit", 10, type=int)
    short = request.args.get("short", 0, type=int)
    product = request.args.to_dict(flat=False).get("q", [])
    return dumps(service.recipe_list(offset, limit, short, [p.lower() for p in product]), ensure_ascii=False)


# get list of products
@app.route("/products")
def products():
    query = request.args.get("q").lower()
    return dumps(service.products(query), ensure_ascii=False)


def main():
    mongo = PyMongo(app)
    from application.service import NoWasteService
    global service
    service = NoWasteService(mongo)
    app.run()


if __name__ == "__main__":
    main()
