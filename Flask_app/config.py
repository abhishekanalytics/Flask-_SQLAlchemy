import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    @staticmethod
    def init_app(app):
      pass

class DevelopmentConfig(Config):
    DEBUG = True
    


config = {
    'development': DevelopmentConfig,
}
