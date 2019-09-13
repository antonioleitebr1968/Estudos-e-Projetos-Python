from time import sleep
import random
from tkinter import *
from functools import partial

AZUL = '#48D1CC'
CINZA = '#A9A9A9'
CINZA_CLARO = '#778899'
CINZA_MAIS_CLARO = '#DCDCDC'
ROXO = '#6A5ACD'
ROSA = '#FF69B4'
AZUL_CLARIN = '#00BFFF'
AZUL_CLARO_DA_PESTE = '#87CEFA'
VERMELHO = '#A52A2A'
VERDE_CLARO = '#00FF00'
SEI_LA = '#FFDEAD'
LARANJA = '#FF8C00'
AZUL_CINZA = '#B0C4DE'
PASTEL = '#E6E6FA'
AZURE = '#F0FFFF'
ROXO_COISADO = '#4B0082'
CINZA2 = '#778899'


cores = [AZUL, CINZA, CINZA_CLARO, CINZA_MAIS_CLARO, ROXO, ROSA, AZUL_CLARIN, AZUL_CLARO_DA_PESTE, VERMELHO,
         VERDE_CLARO, SEI_LA, LARANJA, AZUL_CINZA, PASTEL, AZURE, ROXO_COISADO, CINZA2]
estado = True

def observarEventos():
    pass
    #frame.bind("<Enter>", partial(setInterval, alterarCor, estado))
    #frame.bind("<Leave>", partial(voltarAoNormal))

def voltarAoNormal(event):
    estado = False
    return estado

def escolherCor():
    corEscolhida = random.choice(cores)
    #frame['bg'] = corEscolhida
    return corEscolhida

def alterarCor():
    cor = escolherCor()
    #frame['bg'] = cor

def setInterval(func, event):
    while True:
        sleep(2)
        func()


def simplesmenteMudarCor():
    corEscolhida = random.choice(cores)
    #frame['bg'] = corEscolhida

def callback(event):
    posicao = f'posição X {event.x} e posição Y {event.y}'
    print(posicao)


def observarEventos2():
    #frame.bind("<Enter>", partial(setInterval, simplesmenteMudarCor))
    #frame.bind("<Leave>", partial(simplesmenteMudarCor))
    root.bind("<Button-1>", partial(callback))


root = Tk()
root.resizable(True, True)
#frame = Frame(root, bg='black', width=200, height=200)
#frame.pack()
root['bg'] = AZUL_CLARO_DA_PESTE
observarEventos2()
root.mainloop()



