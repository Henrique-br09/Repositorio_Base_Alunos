from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Olá eu sou o henrique. Sou aluno da Fabrica de programadores'

@app.route('/senha')
def senha():
    return 'Sua senha é 312131'

if __name__ == '__main__':
    app.run(debug=True)



