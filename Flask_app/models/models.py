from sqlalchemy import Column , Integer , String ,Date
from sqlalchemy.ext.hybrid import hybrid_property
from enum import Enum
from datetime import date, timedelta
from ..import db

from werkzeug.security import(
    generate_password_hash,
    check_password_hash
    )



class UserRole(Enum):
    EMPLOYEE="employee"
    MANAGER="manager"
    ADMIN="admin"


class User(db.Model):

    __tablename__ = "Users"


    id= Column(Integer,primary_key=True)
    email=Column(String(300),nullable=False,unique=True)
    username=Column(String(300),nullable=False,unique=True)
    firstname=Column(String(20),nullable=False)
    lastname=Column(String(20),nullable=False)
    mobile_number=Column(String(20),nullable=False)
    hash_password = Column('password', String(350), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    role = Column(db.Enum(UserRole), nullable=False)

    
    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = (today - self.date_of_birth) // timedelta(days=365.2425)
            return age
        return None
    
    @hybrid_property
    def password(self):
        return self.hash_password

    @password.setter
    def password(self, user_password):
        self.hash_password = generate_password_hash(user_password)

    def verify_password(self, user_password):
        return check_password_hash(self.hash_password, user_password)

    def __repr__(self) -> str:
        return '<User %r>' % self.email