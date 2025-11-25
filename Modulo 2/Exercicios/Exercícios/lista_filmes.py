
cont = 1
filmes = []

print('Digite o nome de 3 filmes para a adicionar a lista. ')

while cont <= 3:
    nome = input(f'digite o nome do {cont}° filme: ')
    filmes.append(nome)
    cont = cont + 1

print(filmes)
 
