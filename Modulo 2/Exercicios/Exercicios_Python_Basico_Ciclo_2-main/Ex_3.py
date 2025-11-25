# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE 
cont = 1

quantidade = int(input('digite a quantidade de filmes que deseja: '))

while cont <= quantidade :
    print(cont)
    nome = input(f'qual o nome do filme que deseja adicionar: {cont}° ')
    filmes.append(nome)
    cont = cont + 1 

print(filmes)

# LOOP FOR

qntd = int(input('digite a quantidade de filmes que deseja: '))

for F in range (qntd):
    nome = input('qual o nome do filme que deseja adicionar: ')

    filmes.append(nome)

print(filmes)



















