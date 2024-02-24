from ..models.models import User
from flask import Blueprint
from ..views.auth import AuthView



auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')



auth_bp.add_url_rule(
    rule='/register',
    view_func=AuthView.as_view(
        "register",
        model=User,
    )
)



auth_bp.add_url_rule(
    rule='/login',
    view_func=AuthView.as_view(
        "login",
        model=User
    )
)



auth_bp.add_url_rule(
    rule='/logout',
    view_func=AuthView.as_view(
        "logout"
    )
)
