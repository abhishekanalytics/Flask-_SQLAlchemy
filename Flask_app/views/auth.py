from flask_login import logout_user
from datetime import timedelta
from flask import request,jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from flask_app.models.models import User
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    )
from flask_app.services.auth import (
    get_user_by_email,
    create_user,
    validate_email
    )
from flask_login import logout_user



class AuthView(MethodView):
    def __init__(self, model: User = None) -> None:
        self.model = model
        
     
    def post(self):
        if request.path == "/auth/register":
            username = request.json.get("username")
            email = request.json.get("email")
            firstname = request.json.get("firstname")
            lastname = request.json.get("lastname")
            mobile_number = request.json.get("mobile_number")
            password = request.json.get("password")
            role = request.json.get("role")
            
            if not validate_email(email):
                return jsonify(message="Invalid email format"),400                     
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
            except IntegrityError:
                return jsonify(message="User already exists"),409


        elif request.path == "/auth/login":
            email = request.json.get("email" , None)
            password = request.json.get("password" , None)
            user = get_user_by_email(email)
            if user and user.verify_password(password):
                access_token = create_access_token(
                    identity=user.id,
                    expires_delta=timedelta(minutes=30.0)
                    )
                return jsonify({ "token": access_token}),200
            return jsonify(message="Email or password doesn't match"),400
        

    @jwt_required()
    def get(self):
        if request.path == "/auth/logout":          
            logout_user()
            return jsonify(message='Logout successful')