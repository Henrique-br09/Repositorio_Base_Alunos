from random import randint

numero = randint(1,10)

adivinhar = int(input('tente adivinhar um numero: '))

while adivinhar != numero :
    print('voce errou!!! ')
    adivinhar = int(input('tente adivinhar um numero: '))


print('voce acertou!!!')