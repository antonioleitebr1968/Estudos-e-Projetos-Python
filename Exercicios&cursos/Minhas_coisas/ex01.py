#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
soma = 0
lista = list()
for c in range(0, 4):
    nota = float(input(f'{c + 1}º nota: '))
    lista.append(nota)
    soma += nota
    média = soma / 4
print('As notas foram: ', end='')
for nota in lista:
    print(nota, end=', ')
print(f'\nE a média é de {média:.2f}')


