from flask import request, jsonify
from flask.views import MethodView
from flask_app.models.models import User
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
    )
from ..decorators.decorator import (
    admin_required,
    )
from flask_app.services.users import (
    get_all_users, 
    get_user_by_id,
    update_user,
    delete_user
)



class UserView(MethodView):
    decorators = [jwt_required()]



    def __init__(self, model: User = None) -> None:
        self.model = model



    @admin_required   
    def get(self, id=None):
        if not id:
            users = get_all_users()
            user_list = [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,                   
                    } 
                    for user in users
                ]
            return jsonify({"users": user_list})
        else:
            current_user_id = get_jwt_identity()
            user = get_user_by_id(current_user_id)
            if not user:
                return jsonify({"message": "User not found"}), 404
            user_data = {
                "id": user.id, 
                "username": user.username,
                  "email": user.email
                }
            return jsonify({"user": user_data}) 
    


    @admin_required
    def patch(self, id):
        user = get_user_by_id(id)
        if not user:
            return jsonify({"message": "User not found"}), 404        
        new_data = request.json
        update_user(user, new_data) 
        return jsonify({"message": "User updated successfully"})



    @admin_required
    def delete(self,id):
        user = get_user_by_id(id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        delete_user(user)
        return jsonify({"message": "User deleted successfully"})