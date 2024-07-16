
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config['JWT_SECRET_KEY'] = '1!2"3#4$5%6&7/8(9)0='  # Cambia esto por una clave segura
    app.config['JWT_ALGORITHM'] = 'HS256'  # Algoritmo de firma HMAC con SHA-256
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    
    jwt = JWTManager(app)
    
    with app.app_context():
        from .auth import auth_bp
        from .traducir import traducir_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(traducir_bp)
    
    return app
