from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import config 
 
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    from .views.user import admin
    app.register_blueprint(admin)
    return app