import os # biblioteka systemowa
from flask import Flask, json, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# glowny modul flask 

#konfiguracja bazy danych
basedir = os.path.abspath(os.path.dirname(__file__)) # katalog aplikacji
# __file__ <- sciezka biezacego pliku
# os.path.dirname <- wez katalog ze sciezki (np /a/b/c -> /a/b)
# os.path.abspath <- rozwin sciezke np ~/a/b/c -> /home/user/a/b/c

app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#konfiguracja bazy danych sqlAlchemy

db = SQLAlchemy(app)

db.create_all()

# jaka baza?

# przepis (na razie wersja podstawowa bez wyciagnietych skladnikow itp)
class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(500))
    recipe = db.Column(db.Text)

if Recipe.query.count() == 0:
    # insert initial state
    recipe =Recipe(id = 1, recipe_name='Kielbasa', recipe='Przepis na kielbase')
    recipe2 = Recipe(id = 2, recipe_name='Chleb', recipe='Przepis na chleb')
    recipe3 = Recipe(id = 3, recipe_name='Piwo', recipe='Przepis na piwo')
    db.session.add(recipe)
    db.session.add(recipe2)
    db.session.add(recipe3)
    db.session.commit()
    pass
 
#lista dostepnych przepisow   
@app.route('/recipes')
def recipelist():
    names = []
    recipes = Recipe.query.all()
    for recipe in recipes:
        names.append(recipe.recipe_name)
    response = app.response_class(
        response=json.dumps(names),
        status=200,
        mimetype='application/json'
    )
    return response
    

# konkretny przepis po id
@app.route('/recipes/<recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    
    if recipe is None:
       abort(404)
    else:
       response = app.response_class(
        response=json.dumps({ 'id': recipe.id, 'recipe_name': recipe.recipe_name, 'recipe': recipe.recipe }),
        status=200,
        mimetype='application/json'
    )
    return response


