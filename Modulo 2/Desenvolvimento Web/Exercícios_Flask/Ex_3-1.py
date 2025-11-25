from flask import Flask, render_templete

app = Flask(__name__)

@app.route('/')
def index():
    nome = 'Henrique'
    sobrenome = 'Silva '
    return render_templete('ex_3-1.html', nome=nome, sobrenome=sobrenome)

if __name__ == '__main__':
    app.run(debug=True)
