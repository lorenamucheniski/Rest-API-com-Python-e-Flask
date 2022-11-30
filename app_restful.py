from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {   'id' : '0',
        'Nome': 'Lorena',
        'Habilidades': ['Python', 'Flask']
     },
    {   'id':'1',
        'Nome': 'Diego',
     'Habilidades': ['Python', 'Django']}
]

class Desenvolvedor (Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de id {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return (response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status': 'Sucesso', 'mensagem': 'Registo excluído!'})

api.add_resource(Desenvolvedor, '/dev/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)