import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# main Flask module

# sqlAlchemy database config
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "hard to guess string"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# sqlAlchemy initial

db = SQLAlchemy(app)


# base recipe model
class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255))
    recipe = db.Column(db.Text)
    ingredients = db.Column(db.Text)

    @property
    def serialize(self):
        return {
            "title": self.recipe_name,
            "imgUrl": 'https://loremflickr.com/320/240/food',
            "description": self.recipe,
            "ingredients": self.ingredients.split(',')
        }


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))



db.create_all()

if Recipe.query.count() == 0:
    recipes = [
        Recipe(id=1, recipe_name="Kielbasa", recipe="Przepis na kielbase", ingredients="Kielbasa, Chleb, Ketchup"),
        Recipe(id=2, recipe_name="Chleb", recipe="Przepis na chleb", ingredients="Drzdze, maka, olej"),
        Recipe(id=3, recipe_name="Piwo", recipe="Przepis na piwo", ingredients="drozdze, chmiel"),
        Product(id=1, product_name="Ziemniak"),
        Product(id=2, product_name="Kielbasa"),
        Product(id=3, product_name="Pomidor"),
    ]

    db.session.add_all(recipes)
    db.session.commit()


# all recipes in database
@app.route("/recipes")
def recipelist():
    return jsonify([x.serialize for x in Recipe.query.all()])


# get recipe by id
@app.route("/recipes/<int:recipe_id>")
def recipe(recipe_id: int):
    recipe = Recipe.query.get_or_404(recipe_id)  # get elem by id

    return jsonify(recipe.serialize)

# get list of products
@app.route("/products")
def producs():
    return jsonify([products.product_name for products in Product.query.all() if request.args.get("q").lower() in products.product_name.lower()])

def main():
    app.run()


if __name__ == "__main__":
    main()
