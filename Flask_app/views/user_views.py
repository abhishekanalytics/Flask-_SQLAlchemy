
from flask import Blueprint, request, jsonify
from ..services.user_services import create_user, get_all_users, get_user_by_id, update_user, delete_user

user_views = Blueprint('user_views', __name__)

@user_views.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users=[user.__dict__ for user in users])

@user_views.route('/users', methods=['POST'])
def create_new_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    if not username or not email:
        return jsonify(error="Username and email are required.")
    create_user(username, email)
    return jsonify(message="User created successfully.")

@user_views.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user=user.__dict__)
    else:
        return jsonify(error=f"No user found with id {user_id}.")

@user_views.route('/users/<int:user_id>', methods=['PUT'])
def update_existing_user(user_id):
    data = request.get_json()
    new_username = data.get('username')
    new_email = data.get('email')
    if not new_username or not new_email:
        return jsonify(error="New username and email are required.")
    success = update_user(user_id, new_username, new_email)
    if success:
        return jsonify(message=f"User with id {user_id} updated successfully.")
    else:
        return jsonify(error=f"No user found with id {user_id}.")

@user_views.route('/users/<int:user_id>', methods=['DELETE'])
def delete_existing_user(user_id):
    success = delete_user(user_id)
    if success:
        return jsonify(message=f"User with id {user_id} deleted successfully.")
    else:
        return jsonify(error=f"No user found with id {user_id}.")
