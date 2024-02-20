import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from Flask_app.config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .views.user import bp
    app.register_blueprint(bp)

    return app


config_name = os.getenv('CONFIG', 'default')

app = create_app(config_name)