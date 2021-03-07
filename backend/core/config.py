from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    MONGO_ADDRESS = os.getenv("MONGO_ADDRESS")
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_URI = "mongodb://{}/{}".format(MONGO_ADDRESS, MONGO_DB)

    API_TITLE = "No Waste"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
