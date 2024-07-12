from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/traducir', methods=['POST'])
def traducir_texto():
    # Obtener los datos de la solicitud
    datos = request.get_json()
    idioma_origen = datos['idioma_origen']
    idioma_destino = datos['idioma_destino']
    texto = datos['texto']
    
    # Traducir el texto
    traduccion = translator.translate(texto, src=idioma_origen, dest=idioma_destino)
    
    # Devolver el texto traducido en formato JSON
    return jsonify({'texto_traducido': traduccion.text})

if __name__ == '__main__':
    app.run(debug=False)
