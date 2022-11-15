from flask import Flask, jsonify

app = Flask(__name__)

desenvolvedores = [
    {'Nome': 'Lorena',
     'Habilidades': ['Python', 'Flask']
     },
    {'Nome': 'Diego',
     'Habilidades': ['Python', 'Django']}
]

@app.route('/dev')
def desenvolvedor():
    return jsonify({'nome':'Lorena'})

if __name__ == '__main__':
    app.run(debug = True)
