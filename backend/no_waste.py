import os
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
    return dumps(service.recipe_list(), ensure_ascii=False)


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
