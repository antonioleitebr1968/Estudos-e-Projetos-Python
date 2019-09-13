from tkinter import *

class desenhar():
    def __init__(self, janela):
        self.janela = janela

        self.font1 = ('Arial Black', 20, 'italic')
        self.largura = 900
        self.altura = 900
        self.ultimo = [400, 400]

        self.janela.title('DESENHANDO')

        #criando
        self.f1 = Frame(self.janela, bg='black')
        self.f2 = Frame(self.janela, bg='black')
        self.canvas = Canvas(self.f1, width=800, height=800, bg='white', cursor='star')
        self.bt1 = Button(self.f2, text='CIMA', font=self.font1, bg='yellow', fg='blue', cursor='hand2', command=self.Cima)
        self.bt2 = Button(self.f2, text='ESQUERDA', font=self.font1, bg='yellow', fg='blue', cursor='hand2', comman=self.Esquerda)
        self.bt3 = Button(self.f2, text='DIREITA', font=self.font1, bg='yellow', fg='blue', cursor='hand2', command=self.Direita)
        self.bt4 = Button(self.f2, text='BAIXO', font=self.font1, bg='yellow', fg='blue', cursor='hand2', command=self.Baixo)
        #self.canvas.create_line(400, 400, 400, 400, fill='blue')

        #colocando na tela
        self.f1.pack()
        self.f2.pack()
        self.canvas.pack()
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=LEFT)
        self.bt3.pack(side=LEFT)
        self.bt4.pack(side=LEFT)

        self.janela.mainloop()

    def Direita(self):
        x, y = self.ultimo[0]+ 10, self.ultimo[1]
        self.canvas.create_line(self.ultimo, x, y, fill='blue', width=10)
        self.ultimo = [x, y]


    def Cima(self):
        x, y = self.ultimo[0], self.ultimo[1] - 10
        self.canvas.create_line(self.ultimo, x, y, fill='green', width=10)
        self.ultimo = [x, y]

    def Baixo(self):
        x, y = self.ultimo[0], self.ultimo[1] + 10
        self.canvas.create_line(self.ultimo, x, y, fill='black', width=10)
        self.ultimo = [x, y]

    def Esquerda(self):
        x, y = self.ultimo[0] - 10, self.ultimo[1]
        self.canvas.create_line(self.ultimo, x, y, fill='red', width=10)
        self.ultimo = [x, y]


