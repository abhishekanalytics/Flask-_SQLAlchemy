import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') 
    SECRET_KEY = os.getenv('SECRET_KEY')

    print(SQLALCHEMY_TRACK_MODIFICATIONS)
    
    @staticmethod
    def init_app(app):
      pass

class DevelopmentConfig(Config):
    DEBUG = True
    


config = {
    'development': DevelopmentConfig,
}
