
filmes = {
    'filme' : []
}

qntd = int(input('digite a quantidade de filmes que deseja: '))

for F in range (qntd):
    nome = input('qual o nome do filme que deseja adicionar: ')

    filmes['filme'].append(nome)

print(filmes)

import json

with open('filmes.json', 'w', encoding='utf-8') as arquivo:
    json.dump(filmes, arquivo, indent=4, ensure_ascii=False)


    
