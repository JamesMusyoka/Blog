import os

class Config:

   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
 

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass


class DevConfig(Config):
   

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:37472377@localhost/bloger'
    DEBUG = True


class TestConfig(Config):
 

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://francs:master@localhost/bloger_test'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
