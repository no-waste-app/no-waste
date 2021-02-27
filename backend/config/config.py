from dotenv import load_dotenv
import os
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_ADRESS = os.getenv("MONGO_ADRESS")
    MONGO_DB = os.getenv("MONGO_DB")
    MONGO_URI = "mongodb://{}/{}".format(MONGO_ADRESS, MONGO_DB)



class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
