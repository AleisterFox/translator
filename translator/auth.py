from flask import Blueprint, jsonify, render_template
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)



@auth_bp.route('/token', methods=['GET'])
def get_token():
    # Generar un token sin necesidad de autenticación previa
    access_token = create_access_token(identity='default_user')
    # compressed_token = compress_token(access_token)
    return jsonify(access_token=access_token), 200


@auth_bp.route('/token_page', methods=['GET'])
def token_page():
    return render_template('token.html')