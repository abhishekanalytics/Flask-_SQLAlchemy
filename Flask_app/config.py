import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')

@staticmethod
def init_app(app):
    pass