# ______________________ EX 10 ______________________

positivos = 0
negativos = 0
zeros = 0

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print("\nResultados:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")


