from tkinter import *

#forget significa esquecer
#destroy significa destruir

#OBS:O forget apenas esconde e mantem os elementos na memoria e no espaço da tela...
# já o destroy apaga da memoria e também libera o espaço que eles estavam ocupando na tela.

class Forget_Destroy:

    def __init__(self, janela):

        #Frames
        self.frame1 = Frame(janela, pady=15, bg='blue')
        self.frame2 = Frame(janela, pady=15, bg='blue')
        self.frame3 = Frame(janela, pady=15, bg='blue')
        self.frame4 = Frame(janela, pady=15, bg='blue')
        #self.frame5 = Frame(janela, pady=15, bg='blue')

        #packs
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        #self.frame5.pack()

        #Labels
        self.lb1 = Label(self.frame1, text='Label 1', fg='yellow', font=("Verdana", 25, "bold"), bg='blue')
        self.lb2 = Label(self.frame3, text='Label 2', fg='Yellow', font=("Verdana", 25, "bold"), bg='blue')

        #packs
        #self.lb1.pack()
        #self.lb2.pack()

        #Entrys
        self.ed1 = Entry(self.frame2, font=("Verdana", 25, "bold"))
        self.ed2 = Entry(self.frame4, font=("Verdana", 25, "bold"))

        #packs
        #self.ed1.pack()
        #self.ed2.pack()

        #Checkbuttons
        self.cbEsquerdo_s = False
        self.cbEsquerdo = Checkbutton(janela, text='Box ES', font=('Verdana', 25, 'bold'), cursor='hand2', command=self.Ativa_CBesquerdo)

        self.cbDireito_s = False
        self.cbDireito = Checkbutton(janela, text='Box D', font=('Verdana', 25, 'bold'), cursor='hand2', command=self.Ativa_CBdireito)

        #packs
        self.cbEsquerdo.pack(side=LEFT, anchor=NW)
        self.cbDireito.pack(side=RIGHT, anchor=NE)

        #label para boxs
        self.lbx = Label(janela, text='Boxes desativadas', font=("Verdana", 25, "bold"))

        #packs
        self.lbx.pack(anchor=CENTER)


    #funções

    def Destroi_Elementos(self):
        self.lb1.destroy()
        self.lb2.destroy()
        self.ed1.destroy()
        self.ed2.destroy()


    def Mostra_Elementos(self):
        self.lb1.pack()
        self.lb2.pack()
        self.ed1.pack()
        self.ed2.pack()


    def Some_Elementos(self):
        self.lb1.pack_forget()
        self.lb2.pack_forget()
        self.ed1.pack_forget()
        self.ed2.pack_forget()


    def MSG(self, text, cor = 'red'):
        self.lbx['text'] = text
        self.lbx['fg'] = cor

    def Ativa_CBesquerdo(self):
        self.cbEsquerdo_s = not self.cbEsquerdo_s
        if self.cbEsquerdo_s:
            self.MSG('ativado por Box ESQUERDA')
            self.Mostra_Elementos()
            if self.cbDireito_s:
                self.cbDireito_s = False
                self.cbDireito.deselect()
        else:
            if self.cbEsquerdo_s == False and self.cbDireito_s == False:
                self.MSG('Boxes desativadas', cor='black')
                self.Some_Elementos()
                #self.Destroi_Elementos()
            #self.MSG('cb esquerdo desativado', cor='pink')

    def Ativa_CBdireito(self):
        self.cbDireito_s = not self.cbDireito_s
        if self.cbDireito_s:
            self.MSG('Ativado por Box DIREITA')
            self.Mostra_Elementos()
            if self.cbEsquerdo_s:
                self.cbEsquerdo_s = False
                self.cbEsquerdo.deselect()
        else:
            if self.cbEsquerdo_s == False and self.cbDireito_s == False:
                self.MSG('Boxes desativadas', cor='black')
                self.Some_Elementos()
                #self.Destroi_Elementos()
            #self.MSG('cb direito desativado', cor='pink')

janela = Tk()
Forget_Destroy(janela)
janela.title('testando forget e destroy')
janela['bg'] = 'blue'
janela.geometry('900x600+100+200')
janela.mainloop()
