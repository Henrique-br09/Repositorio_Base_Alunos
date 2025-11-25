from flask import Flask, render_template, request
import json 
import resend

resend.api_key = "re_b1sxbAdR_9pUT7AaGAsw9BWZpztSrPGB1"

with open('contatos.json', 'r', encoding='utf-8')as arquivo:
    contatos = json.load(arquivo)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']

        contato = {}
        contato['nome'] = name
        contato['email'] = email
        contato['mensagem'] = mensagem 

        contatos.append(contato)

        with open('contatos.json', 'w', encoding='utf-8')as arquivo:
            json.dump(contatos, arquivo, indent=4, ensure_ascii=False)

            email_html = f"""
            <h1>Novo contato de {name}! </h1><br>
            <p>Email: {email}</p><br>
            <p>{mensagem}</p>
            """

        r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": "lh120670@gmail.com",
            "subject": "Hello World",
            "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
            })
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    