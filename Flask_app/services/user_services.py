from .. import db
from ..models.models import User

def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

def get_all_users():
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user(user_id, new_username, new_email):
    user = get_user_by_id(user_id)
    if user:
        user.username = new_username
        user.email = new_email
        db.session.commit()
        return True
    return False

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False


