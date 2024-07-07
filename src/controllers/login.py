from flask import request, jsonify
from flask_bcrypt import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
from src.models.user import User
from src import bcrypt

def login():
     email = request.json.get('email', None)
     password = request.json.get('password', None)
     user = User.query.filter_by(email=email).first()
     if user and bcrypt.check_password_hash(user.password_hash, password):
         additional_claims = {"is_admin": user.is_admin}
         access_token = create_access_token(identity=email, additional_claims=additional_claims)
         return jsonify(access_token=access_token), 200
     return 'Wrong email or password', 401 
 
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_as=current_user), 200

@jwt_required()
def admin_data():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

@jwt_required()
def check_admin():
    claims = get_jwt()
    if claims.get('is_admin'):
        return True
    return False