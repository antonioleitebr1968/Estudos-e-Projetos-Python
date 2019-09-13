'''Faça um programa que ajude um jagador da
MEGA SENA a criar palpites. O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma
 lista composta.

from random import randint
from time import sleep

titulo = 'BEM VINDO AO GERADOR DA SORTE'
titulo2 = '< SORTEANDO 10 JOGOS >'
finalizando = '< BOA SORTE! >'
faixa = '-=' * 25
print(f'{faixa}')
print()
print(f'{titulo:^50}')
print()
print(f'{faixa}')
jogos = []
cont = 0
perg = int(input('Quantos jogos quer gerar? '))

for c in range(0, perg):
    jogos.append([])

for j in range(0, perg):
    while len(jogos[cont]) < 6:
        a = randint(1, 60)
        jogos[cont].append(a)
        if a in jogos[cont]:
            a = randint(1, 60)
            jogos[cont].append(a)
    cont += 1
for i in jogos:
    i.sort()
sleep(1)
print()
print(titulo2.center(50, '-'))
for c, v in enumerate(jogos):
    print()
    print(f'Jogo {c + 1}: {v}')
    sleep(1)
print()
print(finalizando.center(50, '='))
'''

# proff =====================================================================

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('         JOGA NA MEGA SENA           ')
print('-' * 30)
quant = int(input('Qauntos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
