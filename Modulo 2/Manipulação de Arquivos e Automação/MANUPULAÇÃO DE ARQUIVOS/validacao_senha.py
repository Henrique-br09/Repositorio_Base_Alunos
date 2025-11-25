email = input('Digite o seu email: ')
senha = input('Digite a sua senha: ')

import json

with open('senha.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

if email == dados['email'] and senha == dados['senha']:
    print('Acesso liberado!')
else:
    print('Acesso negado!')
    