idade = int(input('quantos voce tem? '))
habilita = (input('voce possui habilita? sim ou nao?'))
print(f'posso dirigir?{idade >= 18 and habilita == 'sim' } ')