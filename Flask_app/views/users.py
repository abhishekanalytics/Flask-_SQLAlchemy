from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_app.models.models import User
from ..decorators.decorator import admin_required
from flask_app.services.users import (
    get_all_users, 
    get_user_by_id,
    update_user,
    delete_user
)

class UserView(MethodView):
    def __init__(self, model: User = None) -> None:
        self.model = model
    @jwt_required()
    def get(self, id=None):
        if id is None:
            users = get_all_users()
            user_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
            return jsonify({"users": user_list})
        else:
            user = get_user_by_id(id)
            if not user:
                return jsonify({"message": "User not found"}), 404
            user_data = {"id": user.id, "username": user.username, "email": user.email}
            return jsonify({"user": user_data}) 
    @jwt_required()   
    @admin_required
    def patch(self,id):
        user = get_user_by_id(id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        user.firstname = request.json.get("firstname", user.firstname)
        user.lastname = request.json.get("lastname", user.lastname)
        user.mobile_number = request.json.get("mobile_number", user.mobile_number)
        update_user(user)
        return jsonify({"message": "User updated successfully"})
    @jwt_required()
    @admin_required
    def delete(self,id):
        user = get_user_by_id(id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        delete_user(user)
        return jsonify({"message": "User deleted successfully"})

    def dispatch_request(self, *args, **kwargs):
        view_func = super(UserView, self).dispatch_request
        return view_func(*args, **kwargs)