import os
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps, loads

app = Flask(__name__)
app.config.from_object("config.config.ProductionConfig")
mongo = PyMongo(app)
# main Flask module

# all recipes in database
@app.route("/recipes")
def recipelist():
    recipesmb = mongo.db.recipes.find()
    return dumps(recipesmb, ensure_ascii=False)



# get list of products
@app.route("/products")
def producs():
    ingredient = request.args.get("q").lower()
    ingredientsmb = mongo.db.ingredients.find({"ingredient_name": {'$regex': ingredient}})
    return dumps(ingredientsmb, ensure_ascii=False)

def main():
    app.run()


if __name__ == "__main__":
    main()
