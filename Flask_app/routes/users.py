from flask import Blueprint
from flask_app.models.models import User
from ..views.users import UserView


user_bp = Blueprint('user_bp', __name__, url_prefix='/users')



user_bp.add_url_rule(
    rule='/user',
    view_func=UserView.as_view(
        "get_all_users"
    )
)



user_bp.add_url_rule(
    rule = '/user/<id>',
    view_func = UserView.as_view(
        "display_update_delete",
        model = User
    )
)
