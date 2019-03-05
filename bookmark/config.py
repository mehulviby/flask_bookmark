import os

basedir = os.path.abspath(os.path.dirname(__file__))

# from logging import DEBUG
# app.logger.setLevel(DEBUG)


class Config():
    SECRET_KEY = '\xb6B\xee\xa0\x89\xfb\xddmX\xd6\xa4\xff\x8e\xf8\x15\xe5\x83\xf6\xf0K``\xc7B'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'bookmark.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'bookmark.db')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
