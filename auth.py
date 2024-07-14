from flask import Blueprint, jsonify, render_template
from flask_jwt_extended import create_access_token
import zlib
import base64

auth_bp = Blueprint('auth', __name__)

# def compress_token(token):
#     compressed = zlib.compress(token.encode())
#     return base64.urlsafe_b64encode(compressed).decode()

# def decompress_token(compressed_token):
#     compressed = base64.urlsafe_b64decode(compressed_token)
#     return zlib.decompress(compressed).decode()

@auth_bp.route('/token', methods=['GET'])
def get_token():
    # Generar un token sin necesidad de autenticación previa
    access_token = create_access_token(identity='default_user')
    # compressed_token = compress_token(access_token)
    return jsonify(access_token=access_token), 200


@auth_bp.route('/token_page', methods=['GET'])
def token_page():
    return render_template('token.html')