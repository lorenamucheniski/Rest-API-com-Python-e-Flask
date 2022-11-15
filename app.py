import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'Nome': 'Lorena',
     'Habilidades': ['Python', 'Flask']
     },
    {'Nome': 'Diego',
     'Habilidades': ['Python', 'Django']}
]

@app.route('/dev/<int:id>/', methods = ['GET' , 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

if __name__ == '__main__':
    app.run(debug = True)
