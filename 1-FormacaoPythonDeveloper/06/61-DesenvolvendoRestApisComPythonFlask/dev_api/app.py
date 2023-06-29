from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'íd': 0,
        'nome': 'Flavio',
        'habilidades' : ['Python', 'VB']
     },
    {
        'id' : 1,
        'nome': 'Tamara',
        'habilidades': ['CSS', 'Delphi', 'Python']
     }
]
#devolve um desenvolvedor pelo ID, também altera, deleta um desenvolvedor = utilizando o postman
@app.route("/dev/<int:id>/", methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} nao existe'
            response = {'status': 'erro','mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido. Procure o Administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso`' , 'mensagem ':'item excluido!'})

#Lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len (desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)
