from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import Config

 
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    config.init_app(app)
    db.init_app(app)
    
    from .views.user import admin
    app.register_blueprint(admin)
    return app