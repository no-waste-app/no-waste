from no_waste import no_waste
from no_waste.no_waste import Recipe, Product


import pytest

@pytest.fixture
def client():
    return no_waste.app.test_client()


def test_nonempty_initial_db():
    assert Recipe.query.count() != 0


def test_first_recipe():
    assert Recipe.query.get(1).id == 1


def test_recipe():
    recipe = Recipe.query.get_or_404(1)  # get elem by id
    assert recipe.serialize == {
            "title": "Kielbasa",
            "imgUrl": 'https://loremflickr.com/320/240/food',
            "description": "Przepis na kielbase",
            "ingredients": ["Kielbasa", "Chleb", "Ketchup"]
        }


def test_product(client):
    request = 'm'
    response = client.get("/products?q=Pomidor").json
    assert len(response) == 1
    assert response[0] == "Pomidor"
