#Nome ao contrário em maiúsculas.
# Faça um programa que permita ao usuário digitar o seu nome e em seguida
# mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = 'X'
for letra in range(len(junto) -1, -1, -1):
    print(f'{junto[letra]}', end='')
