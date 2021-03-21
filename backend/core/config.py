from dotenv import load_dotenv
import os

load_dotenv()


def get_mongo_uri(mongo_address, mongo_user, mongo_password, mongo_db):
    if mongo_user and mongo_password:
        return "mongodb://{}:{}@{}/{}?authSource=admin&readPreference=primary&ssl=false".format(
            mongo_user, mongo_password, mongo_address, mongo_db
        )

    return "mongodb://{}/{}".format(mongo_address, mongo_db)


class Config:
    DEBUG = False
    TESTING = False
    MONGO_ADDRESS = os.getenv("MONGO_ADDRESS")
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_URI = get_mongo_uri(MONGO_ADDRESS, MONGO_USER, MONGO_PASSWORD, MONGO_DB)

    API_TITLE = "No Waste"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/api"
    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    JSON_AS_ASCII = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
