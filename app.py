from flask import Flask, send_from_directory
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) 

# Rota para servir o index.html
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# Rota para servir os arquivos estáticos
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('frontend', path)

@app.route('/data/metro')
def metro():
    return send_from_directory('data', 'metro.json')

@app.route('/data/trem')
def trem():
    return send_from_directory('data', 'cptm.json')
if __name__ == '__main__':
    app.run(port=5000)  # Flask rodando na porta 5000
