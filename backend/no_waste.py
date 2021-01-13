import os
from flask import Flask, jsonify
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


db.create_all()

if Recipe.query.count() == 0:
    # insert initial state
    recipe = Recipe(id=1, recipe_name="Kielbasa", recipe="Przepis na kielbase")
    recipe2 = Recipe(id=2, recipe_name="Chleb", recipe="Przepis na chleb")
    recipe3 = Recipe(id=3, recipe_name="Piwo", recipe="Przepis na piwo")
    db.session.add(recipe)
    db.session.add(recipe2)
    db.session.add(recipe3)
    db.session.commit()


# all recipes in database
@app.route("/recipes")
def recipelist():
    return jsonify([recipes.recipe_name for recipes in Recipe.query.all()])


# get recipe by id
@app.route("/recipes/<int:recipe_id>")
def recipe(recipe_id: int):
    recipe = Recipe.query.get_or_404(recipe_id)  # get elem by id

    return jsonify(
        {"id": recipe.id, "recipe_name": recipe.recipe_name, "recipe": recipe.recipe,}
    )


def main():
    app.run()


if __name__ == "__main__":
    main()
