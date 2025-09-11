modelo = input('qual o modelo do carro que foi alugado? ')

dias = float(input("por quantos dias o carro foi alugado " ))

km = float(input("quantos km o carro rodou "))

if modelo == 'maverick':
    diaria = 500

elif modelo == 'bmw':
    diaria = 799.99

elif modelo =='porsche':
    diaria = 1999

elif modelo == 'f-1250':
    diaria = 499

else: 
    diaria = 60

total_dias = dias*diaria
total_km = km * 0.15
valor_total = total_dias + total_km

print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R${valor_total}")