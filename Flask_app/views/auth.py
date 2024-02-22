from flask import request ,jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from flask_app.models.models import UserRole, User
from flask_app.services.auth import get_user_by_email,create_user




class AuthView(MethodView):
    def __init__(self, model: User = None) -> None:
        self.model = model
        
    def post(self):
        if request.path == "/users/register":
            username = request.json.get("username")
            email = request.json.get("email")
            firstname = request.json.get("firstname")
            lastname = request.json.get("lastname")
            mobile_number = request.json.get("mobile_number")
            password = request.json.get("password")
            role = request.json.get("role")
                                  
            try:
                user = create_user(
                    model=self.model,
                    firstname=firstname,
                    lastname=lastname,
                    mobile_number=mobile_number,
                    username=username,
                    email=email,
                    password=password,
                    role=role
                )
                return jsonify(message="User register successfully")
            except Exception as e:
                return jsonify(message="An error occurred while registering user")

        
        elif request.path == "/users/login":
            email = request.json.get("email" , None)
            password = request.json.get("password" , None)
            user = get_user_by_email(email)
            if user and user.verify_password(password):
                return jsonify({"message":"User login successfully"})
            else:   
                return jsonify(message="Email or password doesn't match")


        elif request.path == "/users/logout":
            email = request.json.get("email", None)
            password = request.json.get("password", None)
            user = get_user_by_email(email)
            if user and user.verify_password(password):
                response = jsonify(message="User logged out successfully")
                response.set_cookie('session', '', expires=0)  
                return response
            else:
                return jsonify(message="Email or password doesn't match")