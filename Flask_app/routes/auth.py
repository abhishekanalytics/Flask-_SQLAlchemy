from ..models.models import User
from flask import jsonify,Blueprint
from ..views.auth import AuthView

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

user_bp.add_url_rule(
    rule='/register',
    view_func=AuthView.as_view(
        "register",
        model=User,
    )
)

user_bp.add_url_rule(
    rule='/login',
    view_func=AuthView.as_view(
        "login",
        model=User
    )
)

user_bp.add_url_rule(
    rule='/logout',
    view_func=AuthView.as_view(
        "logout"
    )
)
