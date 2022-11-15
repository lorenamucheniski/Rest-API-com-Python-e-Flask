import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {   'id' : '0',
        'Nome': 'Lorena',
        'Habilidades': ['Python', 'Flask']
     },
    {   'id':'1',
        'Nome': 'Diego',
     'Habilidades': ['Python', 'Django']}
]

#devolver um desenvolvedor pelo ID, fazer alterações e deletar
@app.route('/dev/<int:id>/', methods = ['GET' , 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de id {id} não existe'
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem': 'Registo excluído!'})

# lista todos os desenvolvedores e inclui novos, permite registrar
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])


if __name__ == '__main__':
    app.run(debug = True)
