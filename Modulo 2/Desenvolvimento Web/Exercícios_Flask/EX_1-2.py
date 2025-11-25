from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ola mundo!'

@app.route('/sobre')
def sobre():
    return 'Prazer guri, eu me chamo henrique. Faço curso de programaçao!'

if __name__ == '__main__':
    app.run(debug=True)