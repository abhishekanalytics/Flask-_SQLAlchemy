import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    jwt = JWTManager(app)
    login_manager = LoginManager(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    from .models.models import User
    from flask_app.routes.auth import user_bp
    app.register_blueprint(user_bp)
    return app


config_name = os.getenv('CONFIG', 'default')

app = create_app(config_name)