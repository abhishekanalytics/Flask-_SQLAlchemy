from sqlalchemy import Column , Integer , String ,Date
from Flask_app import db
from sqlalchemy.ext.hybrid import hybrid_property
from enum import Enum


from werkzeug.security import(
    generate_password_hash,
    check_password_hash
    )



class user_role(Enum):
    EMPLOYEE="employee"
    MANAGER="manager"
    ADMIN="admin"


class User(db.Model):

    __tablename__ = "Users"


    id= Column(Integer,primary_key=True)
    email=Column(String(300),nullable=False)
    username=Column(String(300),nullable=False)
    firstname=Column(String(20),nullable=False)
    lastname=Column(String(20),nullable=False)
    mobile_number=Column(String(20),nullable=False)
    hash_password = Column('password', String(350), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    role = Column(db.Enum(user_role), nullable=False)

    
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, user_password):
        self._password = generate_password_hash(user_password)

    def verify_password(self, user_password):
        return check_password_hash(self.hash_password, user_password)

    def __repr__(self) -> str:
        return '<User %r>' % self.email







