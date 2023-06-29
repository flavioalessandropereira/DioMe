from flask import Flask, jsonify, request
import json

app = Flask(__name__)


#@app.route('/<id>')
@app.route('/<int:id>')
def pessoa(id): # digitar 1 : http://127.0.0.1:5000/1
    return jsonify({'id': id, 'nome': 'Flavio', 'profissao': 'DEV'})

#
# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2}) #digitar http://127.0.0.1:5000/soma/10/12/



@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma': total})

if __name__ == '__main__':
    app.run(debug=True)
