# ______________________ EX 09 ______________________

num = int(input("Digite um número: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é primo.")
            break
    else:
        print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")
