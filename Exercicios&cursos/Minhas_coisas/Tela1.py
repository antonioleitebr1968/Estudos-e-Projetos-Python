import tkinter as tk
from Tela2 import Secundaria

class Main(object):
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Main')
        self.janela.geometry('500x500+100+100')
        self.janela.overrideredirect(False)


        self.lb = tk.Label(self.janela, text='sou main')
        self.lb.pack()

        self.bt1 = tk.Button(self.janela, text='chame a secundaria', command=self.chama_secundaria)
        self.bt1.pack()

        self.bt2 = tk.Button(self.janela, text='definir tamanho minimo', command=self.largura_e_altura_minima)
        self.bt2.pack(side=tk.BOTTOM)

        self.bt3 = tk.Button(self.janela, text='quit', command=self.fechar)
        self.bt3.pack(side=tk.BOTTOM)

        self.janela.mainloop()

    def chama_secundaria(self):
        self.lb.destroy()
        self.bt1.destroy()
        self.bt2.destroy()
        Secundaria(self.janela)

    def fechar(self):
        self.janela.quit()

    def largura_e_altura_minima(self):
        self.janela.wm_minsize(width=300, height=300)

    def minimizar(self):
        pass


if __name__ == '__main__':
    Main()
