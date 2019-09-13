"""from tkinter import *

root = Tk()

def callback(event):
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()"""

"""from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()"""

LARGURA = 500
ALTURA = 500

CANVAS_L = 400
CANVAS_A = 400

from tkinter import *
import random


class Jogo(object):
    """
    Classe que organiza os elementos do jogo
    """

    def __init__(self):
        # Criamos o conteiner principal do jogo
        self.root = Tk()
        self.root.geometry('%ix%i' % (LARGURA, ALTURA))
        self.root.resizable(False, False)
        self.root.title('Joguinho Besta')

        # E uma frame para conter o canvas
        self.frame = Frame(bg="black")
        self.frame.pack()

        # Criamos a tela do jogo
        self.canvas = Canvas(self.frame, bg="black", width=CANVAS_L, height=CANVAS_A, cursor='target')
        self.canvas.pack()

        # E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text='START')
        self.começar.pack()

        # self.canvas.create_polygon((100, 200), (150, 250), (250, 250), (300, 200), (300, 100), (250, 50), (150, 50), (100, 100), fill = 'white')

        self.novoJogo()

        self.root.mainloop()

    def novoJogo(self):
        """
        Cria os elementos de um novo jogo
        """
        self.canvas.create_rectangle((CANVAS_L // 2, 350), (CANVAS_L // 2 + 100, 370), fill='green')

        # Lista dos retângulos
        self.r = []

        # E por fim as diversas fileiras de retângulos
        l, c, e = 5, 8, 2  # linhas, colunas e espaçamento
        b, h, y0 = 48, 20, 20  # Base, altura e posição inicial dos retângulos
        for i in range(l):
            cor = random.choice(['#48D1CC', '#A9A9A9', '#6A5ACD', '#FF69B4', '#00BFFF', '#87CEFA'])
            for j in range(c):
                self.canvas.create_rectangle(b * j + (j + 1) * e, i * h + (i + 1) * e + y0, b * j + (j + 1) * e + b,
                                             i * h + (i + 1) * e + y0 + h, fill=cor)

        self.canvas.create_text(CANVAS_L / 2, CANVAS_A / 2, text='Bom jogo!', fill=cor, font=("Verdana", 20, "bold"))


if __name__ == '__main__':
    Jogo()
