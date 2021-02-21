class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = "mongodb://localhost:27017/RecipeDB"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
