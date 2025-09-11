from colorama import init, Fore
init(autoreset=True)

print('| ------------------------ |')
print("|    SISTEMA DE PROVA      |")
print('| ------------------------ |')

nome = (input('Nome do aluno:'))

nota_1 = float(input('nota da primeira prova:'))
nota_2 = float(input('nota da segunda prova:'))
nota_3 = float(input("nota da terceira prova:"))
print("| ------------------------ |")
media = (nota_1 + nota_2 + nota_3) /3 
if media >= 5:
    print(Fore.GREEN+f"|Aluno: {nome} Aprovado")
else:
    print(Fore.RED+f'aluno: {nome} Reprovado')
print('| ------------------------ |')

