print('______________________________')
print('________SISTEMA PROVA_________')
print('______________________________')

prova = int(input('quantas provas deseja? '))
contador = 1
soma = 0

while contador <= prova:
    numero = float(input(f'nota da prova {contador}: '))
    contador += 1
    soma = soma + numero

media = soma/prova
print(f'sua media é de {media}')




















