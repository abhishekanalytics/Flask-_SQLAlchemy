from flask import jsonify,Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return jsonify({"msg":"This is basic application factory"})
