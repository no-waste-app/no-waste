import os
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# main Flask module

# sqlAlchemy database config
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlAlchemy initial

db = SQLAlchemy(app)

db.create_all()

# base recipe model
class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255))
    recipe = db.Column(db.Text)

def main():
    if Recipe.query.count() == 0:
        # insert initial state
        recipe = Recipe(id=1, recipe_name='Kielbasa', recipe='Przepis na kielbase')
        recipe2 = Recipe(id=2, recipe_name='Chleb', recipe='Przepis na chleb')
        recipe3 = Recipe(id=3, recipe_name='Piwo', recipe='Przepis na piwo')
        db.session.add(recipe)
        db.session.add(recipe2)
        db.session.add(recipe3)
        db.session.commit()
        pass


# all recipes in database
@app.route('/recipes')
def recipelist():
    names = []
    recipes = Recipe.query.all()
    for recipe in recipes:
        names.append(recipe.recipe_name)
    return jsonify(names)


# get recipe by id
@app.route('/recipes/<int:recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id) #get elem by id

    if not recipe:
        abort(404)
    else:
        return jsonify({'id': recipe.id, 'recipe_name': recipe.recipe_name, 'recipe': recipe.recipe})
