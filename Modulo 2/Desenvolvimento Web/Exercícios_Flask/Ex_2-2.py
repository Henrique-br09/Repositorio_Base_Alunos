from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Hello, My name is Henrique and I take a programming course, and I am a programmer!!!'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'ola {nome}'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return(f'o dobro de {numero} é {numero*2}')

if __name__ == '__main__':
    app.run(debug=True)

