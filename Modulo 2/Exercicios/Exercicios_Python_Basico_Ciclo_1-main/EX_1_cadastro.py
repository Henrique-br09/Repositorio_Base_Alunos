# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print(' | ---------------------------- | ')
print(' | --------- CADASTRO --------- | ')
print(' | ---------------------------- | ') 

nome = input('| qual o seu nome? ') 
idade = int(input('| qual sua idade? '))
email = input('| qual o seu email? ')
senha = input('| qual a sua senha? ')

print(' | ----------------------------| ')
print(' | ---- USUARIO CADASTRADO ----| ')
print(f' | Seja bem vindo(a) {nome} ')
print(f' | Email: {email}')
print(' | ----------------------------| ')

