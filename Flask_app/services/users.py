from ..models.models import User
from .. import db

def get_all_users():
    return User.query.all()

def get_user_by_id(id):
    user = User.query.get(id)
    return user

def update_user(user):
    db.session.commit()

def delete_user(user):
    db.session.delete(user)
    db.session.commit()