from flask import jsonify
from functools import wraps
from flask_app.models.models import User
from flask_jwt_extended import get_jwt_identity



def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = User.query.get( current_user_id)
        if current_user.role.value=="admin":
            return f(*args, **kwargs)
        else:
            return jsonify(error="Unauthorized")
    return decorated_function


def manager_required(f):
   @wraps(f)
   def decorated_function(*args, **kwargs):
       current_user_id = get_jwt_identity()
       current_user = User.query.get(current_user_id)
       if current_user.role.value == "manager" or current_user.role.value == "admin": 
           return f(*args, **kwargs)
       else:
           return jsonify(error="Unauthorized")
   return decorated_function


def employee_required(f):
   @wraps(f)
   def decorated_function(*args, **kwargs):
       current_user_id = get_jwt_identity()
       current_user = User.query.get(current_user_id)
       if current_user.role.value == "employee" or current_user.role.value == "admin":
           return f(*args, **kwargs)
       else:
           return jsonify(error="Unauthorized")
   return decorated_function
