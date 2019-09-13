# exercicio 13
#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#  e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )
from math import trunc
lista = list()
lista2 = list()
cont = soma = 0
while True:
    mês = str(input('Digite o nome do mês: '))
    temperatura = float(input(f'Digite a temperatura referente ao mês {mês} em graus celsius º'))
    cont += 1
    soma += temperatura
    lista.append(mês)
    lista2.append(temperatura)
    print('-' * 60)
    if cont == 12:
        break
média = trunc(soma) / 12#média anual das temperaturas
print(f'A média de temperatura anual foi de {média:.0f}ºc')
print('As temperaturas a cima da média foram: ', end=' ')
for t in lista2:
    if t > média:
        print(f'{t}ºc', end=', ')
print('\nAcabou')
