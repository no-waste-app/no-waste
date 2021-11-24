import json

import pytest
from backend.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# test default limit - 10 rows
def test_limit_results_to_10_by_default(client):
    rv = client.get('/api/recipes/')
    data = json.loads(rv.data)
    assert 10 == len(data)


# test custom limit
def test_limit_results_to_value(client):
    rv = client.get('/api/recipes/?limit=5')
    data = json.loads(rv.data)
    assert 5 == len(data)


# test if limit 20 rows contains default 10 rows and next 10 rows
def test_offset(client):
    rv = client.get('/api/recipes/')
    data = json.loads(rv.data)
    rv_offset = client.get('/api/recipes/?offset=10')
    data_offset = json.loads(rv_offset.data)
    rv_all = client.get('/api/recipes/?limit=20')
    data_all = json.loads(rv_all.data)
    assert data == data_all[:10]
    assert data_offset == data_all[10:20]


# all recipes contains ingredient from query?
def test_search_query(client):
    rv = client.get('/api/recipes/?q=woda')
    data = json.loads(rv.data)
    for recipe in data:
        assert "woda" in [x["name"] for x in recipe["ingredients"]]


# all recipes contains ingredients quantity ?
def test_ingredients_quantity(client):
    rv = client.get('/api/recipes/')
    data = json.loads(rv.data)
    for recipe in data:
        for ingredient in recipe["ingredients"]:
            assert ingredient["quantity"] is not None

# test short version doesnt contains directions
def test_short_version(client):
    rv = client.get('/api/recipes/?short=1')
    data = json.loads(rv.data)
    for recipe in data:
        assert "directions" not in recipe
        assert "title" in recipe

# test product api 
def test_product_api(client):
    rv = client.get('/api/products/?q=woda')
    data = json.loads(rv.data)
    for product in data:
       assert "woda" in product["name"]

# different endpoint returns false
def test_bad_request(client):
    rv=client.get('/api/wrong/?q=woda')
    assert rv.status_code == 404