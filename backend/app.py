from flask import Flask
from flask_smorest import Api

from backend.api import register_api
from backend.core.db import mongo

def create_app():
    app = Flask(__name__)
    app.config.from_object("backend.core.config.ProductionConfig")
    mongo.init_app(app)

    api = Api(app)
    register_api(api)

    return app
