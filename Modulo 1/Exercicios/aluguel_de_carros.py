dias = float(input("por quantos dias o carro foi alugado " ))
km = float(input("quantos km o carro rodou "))
total_dias = dias * 60 
total_km = km * 0.15
valor_total = total_dias + total_km
print(f"Você andou {km}km por {dias} dias, então o preço a pagar é R${valor_total}.")