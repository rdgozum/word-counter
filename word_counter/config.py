import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_DEV_URI")


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_TEST_URI")
