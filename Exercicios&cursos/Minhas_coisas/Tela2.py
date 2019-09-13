import tkinter as tk

class Secundaria:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Secundario')
        self.janela.geometry('200x200+100+100')

        self.lb = tk.Label(self.janela, text='Sou secundario')
        self.lb.pack()

