from sqlalchemy import Column , Integer , String 
from Flask_app import db

class User(db.Model):

    __tablename__ = "Users"

    id= Column(Integer,primary_key=True)
    email=Column(String(300),nullable=False)
    username=Column(String(300),nullable=False)
    firstname=Column(String(20),nullable=False)
    lastname=Column(String(20),nullable=False)
    mobile_number=Column(String(20),nullable=False)
    age = db.Column(db.Integer)