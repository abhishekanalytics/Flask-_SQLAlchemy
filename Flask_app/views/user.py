from flask import jsonify,Blueprint
bp = Blueprint('bp', __name__, url_prefix='/users')
@bp.route('/use')
def index():
    return jsonify({"msg":"This is a block of my cjjain and whatever you want than client ro be useful authantiucation using the syntax "})