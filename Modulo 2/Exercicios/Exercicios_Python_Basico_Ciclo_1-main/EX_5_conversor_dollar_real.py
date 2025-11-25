# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

cotacao = float(input('digite a cotação do dollar: ')) 

conversao = float(input('digite o valor em dollar a ser convertido para real: '))

total_valor = (cotacao * conversao )

print(f'o valor em reais é: {total_valor}' )







