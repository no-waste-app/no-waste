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

    @property
    def serialize(self):
        return {
            "title": self.recipe_name,
            "imgUrl": None,
            "description": self.recipe,
            "ingredients": ["Czekolada", "Chleb"]
        }


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))



db.create_all()

if Recipe.query.count() == 0:
    # insert initial state
    Recipe.query.delete()
    Product.query.delete()
    recipe = Recipe(id=1, recipe_name="Kielbasa", recipe="Przepis na kielbase")
    recipe2 = Recipe(id=2, recipe_name="Chleb", recipe="Przepis na chleb")
    recipe3 = Recipe(id=3, recipe_name="Piwo", recipe="Przepis na piwo")
    product = Product(id=1, product_name="Ziemniak")
    product1 = Product(id=2, product_name="Kielbasa")
    product2 = Product(id=3, product_name="Pomidor")
    db.session.add(recipe)
    db.session.add(recipe2)
    db.session.add(recipe3)
    db.session.add(product)
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()


# all recipes in database
@app.route("/recipes")
def recipelist():
    return jsonify([x.serialize for x in Recipe.query.all()])


# get recipe by id
@app.route("/recipes/<int:recipe_id>")
def recipe(recipe_id: int):
    recipe = Recipe.query.get_or_404(recipe_id)  # get elem by id

    return jsonify(
        {"id": recipe.id, "recipe_name": recipe.recipe_name, "recipe": recipe.recipe, }
    )

# get list of products
@app.route("/product")
def producs():
    return jsonify([products.product_name for products in Product.query.all() if request.args.get("q").lower() in products.product_name.lower()])

def main():
    app.run()


if __name__ == "__main__":
    main()
