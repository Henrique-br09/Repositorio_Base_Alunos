# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

opção = int(input('Escolha uma opção:'))

if opção == 1:
    print('Dollar para real') 

    cotacao1 = float(input( 'informe a cotação atual do dollar:'))

    quantidade1 = float(input('informe a quantidade de reais:'))

    total_valor = cotacao1 * quantidade1

    print(f'a quantidade em reais é {total_valor}')

elif opção == 2:
    print('Real para dollar')
    
    cotacao2 = float(input('informe a cotação atual do dollar: '))

    quantidade2 = float(input('informe a quantidade em reais: '))

    total_valor2 = quantidade2 / cotacao2

    print(f'o valor em dolares é: {total_valor2:.2f}')
    
else:
    print('numero incorreto')










