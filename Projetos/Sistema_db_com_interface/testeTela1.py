from tkinter import *
from functools import partial ##necessario para passar parametros a uma função sem invoca-lá
import mysql.connector
from mysql.connector import errorcode

class Menu(object):
    def __init__(self):
        #############VARIÁVEIS CONTENDO CORES##################
        self.AZUL = '#48D1CC'
        self.CINZA = '#A9A9A9'
        self.CINZA_CLARO = '#778899'
        self.CINZA_MAIS_CLARO = '#DCDCDC'
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
        self.AZURE = '#F0FFFF'
        self.ROXO_COISADO = '#4B0082'
        self.CINZA2 = '#778899'
        self.OrangeRed = '#FF4500'
        self.Gold = '#FFD700'

        #fontes -------------------------------------
        self.font = ('Verdana', 25, 'bold')
        self.font2 = ('papyrus', 17, 'bold')
        self.fontGrande = ('papyrus', 30, 'bold')
        self.font3 = ('Verdana', 15, 'bold')
        self.font4 = ('Bauhaus 93', 25, 'bold')
        self.font5 = ('Verdana', 23, 'bold')

        self.janela = Tk()
        self.janela.title("Agenda")
        # self.janela.wm_iconbitmap('imagens\\g1.ico')
        self.janela.resizable(False, False)
        self.janela.geometry("1000x700+50+100")
        self.janela["bg"] = self.CINZA

        # mudanças --------------------------------
        self.font4 = ('Bauhaus 93', 25, 'bold')
        self.janela.title("Agenda")
        self.janela.geometry("800x600+50+100")
        self.janela["bg"] = self.CINZA

        self.congiButtons = {"bg": self.AZUL_CINZA, "fg": "black",
                             "font": self.font2, "cursor": "hand2",
                             "bd": 2, "relief": GROOVE, 'width': 30}

        self.congiLabel2 = {"bg": self.CINZA, "fg": 'black',
                            "font": self.font4, "pady": 10}

        self.congiLabel3 = {"bg": self.CINZA, "fg": self.VERMELHO,
                            "font": self.font4, "pady": 10}
        # -----------------------------------------
        self.framePai = Frame(self.janela, bg=self.CINZA)
        self.framePai.pack()

        self.lb1 = Label(self.framePai, text="ALTERAR UM CONTATO EXISTENTE", **self.congiLabel2)
        self.lb1.grid(row=0, column=0)

        self.lb2 = Label(self.framePai, text="ESCOLHA UMA DAS OPÇÕES PARA \nLOCALIZAR O CONTATO", **self.congiLabel3)
        self.lb2.grid(row=1, column=0)

        self.btID = Button(self.framePai, text="ID", **self.congiButtons,
                           command=self.destruirMenuAgenda)
        self.btID.grid(row=2, column=0)

        self.btNome = Button(self.framePai, text="NOME", **self.congiButtons)
        self.btNome.grid(row=3, column=0)

        self.btTelefone = Button(self.framePai, text="TELEFONE", **self.congiButtons)
        self.btTelefone.grid(row=4, column=0)

        self.btCelular = Button(self.framePai, text="CELULAR", **self.congiButtons)
        self.btCelular.grid(row=5, column=0)

        self.btMenu = Button(self.framePai, text="MENU PRINCIPAL", **self.congiButtons)
        self.btMenu.grid(row=6, column=0)

        self.chamarEventosBtns3()

        self.janela.mainloop()



    def configurarBt(self, obj, bg, bd, width, font, event):
        obj.configure(bg=bg, bd=bd, width=width, font=font)


    def destruirMenuAgenda(self):
        self.framePai.destroy()

    def chamarEventosBtns3(self):
        self.btID.bind('<Enter>', partial(self.configurarBt, self.btID, self.VERMELHO, 10, 32, self.font5))
        self.btID.bind('<Leave>', partial(self.configurarBt, self.btID, self.AZUL_CINZA, 2, 30, self.font2))

        self.btNome.bind('<Enter>', partial(self.configurarBt, self.btNome, self.VERMELHO, 10, 32, self.font5))
        self.btNome.bind('<Leave>', partial(self.configurarBt, self.btNome, self.AZUL_CINZA, 2, 30, self.font2))

        self.btTelefone.bind('<Enter>', partial(self.configurarBt, self.btTelefone, self.VERMELHO, 10, 32, self.font5))
        self.btTelefone.bind('<Leave>', partial(self.configurarBt, self.btTelefone, self.AZUL_CINZA, 2, 30, self.font2))

        self.btCelular.bind('<Enter>', partial(self.configurarBt, self.btCelular, self.VERMELHO, 10, 32, self.font5))
        self.btCelular.bind('<Leave>', partial(self.configurarBt, self.btCelular, self.AZUL_CINZA, 2, 30, self.font2))

        self.btMenu.bind('<Enter>', partial(self.configurarBt, self.btMenu, self.VERMELHO, 10, 32, self.font5))
        self.btMenu.bind('<Leave>', partial(self.configurarBt, self.btMenu, self.AZUL_CINZA, 2, 30, self.font2))

if __name__ == '__main__':
    Menu()
