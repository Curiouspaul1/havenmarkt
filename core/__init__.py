from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config import config

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    CORS(app)

    # register bps
    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app
