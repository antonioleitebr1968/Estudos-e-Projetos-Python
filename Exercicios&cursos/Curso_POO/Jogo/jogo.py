from tkinter import *
from constantes import *
import random

class Jogo(object):

    def __init__(self):
        #Criando área principal do jogo
        self.root = Tk()
        self.root.geometry(f'{LARGURA}x{ALTURA}')
        self.root.resizable(False, False)
        self.root.title('Primeiro jogo')

        #frame para conter o canvas
        self.frame = Frame(bg='blue')
        self.frame.pack()

        #código de criação do canvas
        self.canvas = Canvas(self.frame, bg='blue', width=CANVAS_L, height=CANVAS_A, cursor='target')
        self.canvas.pack()

        #criando objetos dentro do canvas
        #self.canvas.create_line(10, 10, 350, 350, fill='white')
        #self.canvas.create_polygon((100, 200), (150, 250), (250, 250), (300, 200), (300, 100), (250, 50), (150, 50), (100, 100), fill='white')


        self.começar = Button(self.root, text='INICIAR', command=self.começa)
        self.começar.pack()
        self.novoJogo()



        self.root.mainloop()



    def novoJogo(self):
        #criação dos elementos do jogo
        self.canvas.create_rectangle((CANVAS_L//2, 360), (CANVAS_L//2 + 80, 380), fill='white')


        #criando a bolinha do jogo
        raio = 30
        p = (100, 200)
        self.canvas.create_oval(p[0], p[1], p[0] + raio, p[1] + raio, fill='red', outline='white')
        self.b_vx = self.b_vy = 3
        self.b_x, self.b_y = p
        #mudar o estado para jogando
        self.jogando = True


        #lista dos retangulos
        self.r = []
        l, c, e = 5, 8, 2#linhas, colunas e espaçamentos
        b, h, y0 = 48, 20, 50#base, altura e posição inicial




        for i in range(l):
            cor = random.choice(['black', 'orange', 'white', 'Grey', 'yellow', 'green', 'purple'])
            for j in range(c):
                self.canvas.create_rectangle(b*j+(j+1)*e, i*h+(i+1)*e + y0, b*j+(j+1)*e + b, i*h+(i+1)*e + y0 + h, fill=cor)

        self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text='Bem Vindos!!', fill='white', font='Verdana, 12')


    def começa(self):
        #iniciar o jogo
        self.jogar()


    def jogar(self):
        #Vai ser executado enquanto o jogador estiver jogando
        if self.jogando:
            self.update()
            self.root.after(10, self.jogar())
        else:
            self.acabou(self.msg)


    def update(self):
        #movimento da bola
        self.canvas.move('bola', self.b_vx, self.b_vy)

        #atualizar o movimento da bola e sua posição
        self.b_x += self.b_vx
        self.b_y += self.b_vy

        #verificar se a bola está batendo dos lados
        if self.b_x > CANVAS_L - self.raio or self.b_x < 0:
            self.b_vx *= -1

if __name__ == '__main__':
    Jogo()
