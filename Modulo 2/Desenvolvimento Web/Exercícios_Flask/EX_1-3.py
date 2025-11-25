from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ola mundo!'

@app.route('/sobre')
def sobre():
    return 'Prazer guri, eu me chamo henrique. Faço curso de programaçao!'

@app.route('/ola/<nome>')
def ola(nome):
    if nome == 'henrique':
        return f'Olá Chefe, Seja muito bem vindo Novamente.'
    
    return f'Olá {nome}!'
     

if __name__ == '__main__':
    app.run(debug=True)