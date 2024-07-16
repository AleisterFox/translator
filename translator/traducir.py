from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required
from googletrans import Translator

traducir_bp = Blueprint('traducir', __name__)
translator = Translator()

@traducir_bp.route('/traducir', methods=['POST', 'OPTIONS'])
@jwt_required()
def traducir_texto():
    if request.method == 'OPTIONS':
        return jsonify({'Allow': 'POST'}), 200
    
    datos = request.get_json()
    idioma_origen = datos.get('idioma_origen')
    idioma_destino = datos.get('idioma_destino')
    texto = datos.get('texto')
    
    if not idioma_origen:
        try:
            idioma_origen = translator.detect(texto).lang
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    if not idioma_destino or not texto:
        return jsonify({'error': 'Faltan parámetros'}), 400
    
    try:
        traduccion = translator.translate(texto, src=idioma_origen, dest=idioma_destino)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'texto_traducido': traduccion.text})


@traducir_bp.route('/')
def index():
    return render_template('index.html')