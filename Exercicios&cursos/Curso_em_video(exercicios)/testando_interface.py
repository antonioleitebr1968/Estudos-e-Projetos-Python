"""from random import randint
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
        if a in jogos[0]:
            a = randint(1, 60)
            jogos[cont].append(a)
    cont += 1
sleep(1)
print()
print(titulo2.center(50, '-'))
print()
for c, v in enumerate(jogos):
    print(f'Jogo {c + 1}: {v}')
    sleep(1)
print()
print(finalizando.center(50, '='))"""

from tkinter import *

titulo = 'BEM VINDO AO GERADOR DA SORTE'
titulo2 = '< SORTEANDO 10 JOGOS >'
finalizando = '< BOA SORTE! >'
faixa = '-=' * 25

janela = Tk()

lb1 = Label(janela, text=titulo, bg='yellow')
lb1.grid(row=0, column=0)




janela.geometry('500x500+500+300')
janela.mainloop()
#continua depois...
