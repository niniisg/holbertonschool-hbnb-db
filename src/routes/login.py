from flask import Blueprint
from src.controllers.login import login, protected, admin_data

loging_bp = Blueprint("loging", __name__, url_prefix="/login")
loging_bp.route("/", methods=["POST"])(login)

authentic_bp = Blueprint("protected", __name__, url_prefix="/protected")
authentic_bp.route("/", methods=["GET"])(protected)

admn_bp = Blueprint("admin", __name__, url_prefix="/admin/data")
admn_bp.route("/", methods=["POST", "DELETE"])(admin_data)