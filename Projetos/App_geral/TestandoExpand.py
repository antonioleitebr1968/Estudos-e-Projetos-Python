from tkinter import *


class Teste():
    def __init__(self):
        #fonte
        self.font = ('Vijaya', 34, 'bold')

        #############VARIÁVEIS CONTENDO CORES##################
        self.AZUL = '#48D1CC'
        self.CINZA = '#A9A9A9'
        self.ROXO = '#6A5ACD'
        self.ROSA = '#FF69B4'
        self.AZUL_CLARIN = '#00BFFF'
        self.AZUL_CLARO_DA_PESTE = '#87CEFA'
        self.VERMELHO = '#A52A2A'
        self.VERDE_CLARO = '#00FF00'
        self.SEI_LA = '#FFDEAD'
        self.LARANJA = '#FF8C00'
        self.AZUL_CINZA = '#B0C4DE'
        self.PASTEL = '#E6E6FA'
        #######################################################

        self.janela = Tk()
        self.janela.title("Expand")
        self.janela.geometry("1280x720+200+200")
        self.janela.resizable(True, True)
        self.janela["bg"] = self.PASTEL


        self.frame_um = Frame(self.janela, bg=self.ROSA)
        self.frame_um.pack(expand=1, fill=X)
        self.label1 = Label(self.frame_um, text="Label um", font=self.font, bg=self.ROSA, fg="yellow", pady=10)
        self.label1.pack()

        self.frame_dois = Frame(self.janela, bg=self.ROSA)
        self.frame_dois.pack(expand=1, fill=X)
        self.label2 = Label(self.frame_dois, text="Label dois", font=self.font, bg=self.ROSA, fg="yellow", pady=10)
        self.label2.pack()

        self.frame_tres = Frame(self.janela, bg=self.ROSA)
        self.frame_tres.pack(expand=1, fill=X)
        self.label2 = Label(self.frame_tres, text="Label três", font=self.font, bg=self.ROSA, fg="yellow", pady=10)
        self.label2.pack()

        self.frame_quatro = Frame(self.janela, bg=self.ROSA)
        self.frame_quatro.pack(expand=1, fill=X)
        self.label2 = Label(self.frame_quatro, text="Label quatro", font=self.font, bg=self.ROSA, fg="yellow", pady=10)
        self.label2.pack()


        self.janela.mainloop()




Teste()