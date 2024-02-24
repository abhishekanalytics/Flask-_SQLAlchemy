from ..models.models import User
from .. import db

def get_all_users():
    return User.query.all()

def get_user_by_id(id):
    user = User.query.get(id)
    return user

# def update_user(user):
#     db.session.commit()

def update_user(user, new_data):
    # Update user attributes with new data
    user.firstname = new_data.get("firstname", user.firstname)
    user.lastname = new_data.get("lastname", user.lastname)
    user.mobile_number = new_data.get("mobile_number", user.mobile_number)
    
    # Commit changes to the database
    db.session.commit()


def delete_user(user):
    db.session.delete(user)
    db.session.commit()