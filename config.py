import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.getcwd())


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('secretkey')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir}/dev.db"
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config = {
    "default": DevConfig,
    "development": DevConfig,
    "production": ProdConfig
}
