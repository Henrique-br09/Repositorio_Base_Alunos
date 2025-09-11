print('|-------------------------------|')
print('|        calculadora            |')
print('|-------------------------------|')
print('| 1- Soma')
print('| 2- Subtração')
print('| 3- Multiplicação')
print('| 4- Divisao')
print('|-------------------------------|')

escolha = float(input('| Escolha uma das opçoes: '))

primeiro = float(input('| digite o primeiro numero: '))

segundo = float(input('| digite o segundo numero: '))

if escolha == 1:
    print(f'o resultado é {primeiro + segundo}')
elif escolha == 2:
    print(f'o resultado é {primeiro - segundo}')
elif escolha == 3:
    print(f'o resultado é {primeiro * segundo}')
elif escolha == 4: 
    print(f'o resultado é {primeiro / segundo}')
else:
    print('ERRO. Tente novamente e digite um numero valido!')













