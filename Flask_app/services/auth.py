from typing import Any
import re
from ..import db
from ..models.models import User


def create_user(model: Any, 
                username: str, 
                email: str,
                password: str,
                role: str,
                firstname:str,
                lastname:str,
                mobile_number:int,
                ): 
    user = model(
        username = username,
        email = email,
        password=password,
        firstname=firstname,
        lastname=lastname,
        mobile_number=mobile_number,
        role = role
    )
    db.session.add(user)
    db.session.commit()



def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user




def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    
