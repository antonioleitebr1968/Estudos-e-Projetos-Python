from tkinter import *

class Marcar:
    def __init__(self, janela):
        AZUL = '#77B7F7'
        self.font = ('Vijaya', 25, 'bold')
        #criando Frames
        self.frameSuperior = Frame(janela, bg='black', pady=25)

        #criando Label e Checkbutton
        self.labelSuperior = Label(self.frameSuperior, text='janela', font=('Vijaya', 40, 'bold'), bg='black', fg='yellow')

        self.cbEsquerdo_s = False
        self.cbEsquerdo = Checkbutton(janela, text='Box ES', font=('Verdana', 35, 'bold'), bg='yellow', cursor='hand2',command=self.Ativa_CBesquerdo)

        self.cbDireito_s = False
        self.cbDireito = Checkbutton(janela, text='Box D', font=('Verdana', 35, 'bold'), bg='yellow', cursor='hand2',command=self.Ativa_CBdireito)

        #colocando tudo na tela:
        #Frame superior
        self.frameSuperior.pack(side=TOP, fill=X)
        self.labelSuperior.pack()
        #Frame esquerdo
        self.cbEsquerdo.pack(side=LEFT, anchor=NW)
        #Frame direito
        self.cbDireito.pack(side=RIGHT, anchor=NE)

        self.ed1 = Entry(janela, font=('Verdana', 25, 'bold'), fg='black', bg=AZUL)
        self.ed1.pack()

        self.frameButton = Frame(janela, pady=15, bg=AZUL)
        self.frameButton.pack()
        self.bt1 = Button(self.frameButton, text='Precione', font=('Verdana', 25, 'bold'), fg='blue', cursor='hand2',command=self.MudaEntradaDeTexto)
        self.bt1.pack()

        self.frameButton2 = Frame(janela, pady=15, bg=AZUL)
        self.frameButton2.pack()
        self.bt2 = Button(self.frameButton2, text='Apagar', font=('Verdana', 25, 'bold'), fg='blue', cursor='hand2',command=self.ApagaTexto)
        self.bt2.pack()

        # logo do aplicativo
        logo = PhotoImage(file='C:\\Users\\user\\Pictures\\PythonLogo.gif')  # caminho da gif
        self.logo = Label(janela)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()


    def ApagaTexto(self):
        self.ed1.delete(0, END)# deleta do indece 0 até o final


    def MudaEntradaDeTexto(self):
        self.ed1.insert(END, ' Sucesso')#coloca o texto "Sucesso" no final
        self.ed1['fg'] = 'yellow'


    def MSG(self, text, cor = 'red'):
        self.labelSuperior['text'] = text
        self.labelSuperior['fg'] = cor


    def Ativa_CBesquerdo(self):
        self.cbEsquerdo_s = not self.cbEsquerdo_s
        if self.cbEsquerdo_s:
            self.MSG('cb esquerdo ativado')
            if self.cbDireito_s:
                self.cbDireito_s = False
                self.cbDireito.deselect()
        else:
            if self.cbEsquerdo_s == False and self.cbDireito_s == False:
                self.MSG('janela', cor='yellow')
            #self.MSG('cb esquerdo desativado', cor='pink')

    def Ativa_CBdireito(self):
        self.cbDireito_s = not self.cbDireito_s
        if self.cbDireito_s:
            self.MSG('cb direito ativado')
            if self.cbEsquerdo_s:
                self.cbEsquerdo_s = False
                self.cbEsquerdo.deselect()
        else:
            if self.cbEsquerdo_s == False and self.cbDireito_s == False:
                self.MSG('janela', cor='yellow')
            #self.MSG('cb direito desativado', cor='pink')



janela = Tk()
#Marcar(janela)
janela.title('TESTE')
Marcar(janela)
AZUL = '#77B7F7'
janela['bg'] = AZUL
"""cb1 = Checkbutton(janela, text='fodase')
cb1.pack()"""
janela.geometry('1000x600+100+100')
janela.mainloop()





a = "arrow"    #"flecha"
b = "circle"   #"círculo"
c = "clock"    #"relógio"
d = "cross"    #"Cruz"
e = "dotbox"   #"dotbox"
f = "exchange" #"troca"
j = "fleur"    #"fleur"
h = "heart"    #"coração"
l = "heart"    #"coração"
m = "man"      #"homem"
n = "mouse"    #"rato"
o = "pirate"   #"pirata"
p = "plus"     #"mais"
q = "shuttle"  #"transporte"
r = "sizing"   #"dimensionamento"
s = "spider"   #"aranha"
t = "spraycan" #"lata de spray"
u = "star"     #"Estrela"
v = "target"   #"alvo"
w = "tcross"   #"tcross"
x = "trek"     #"trek"
y = "watch"    #"Assistir"
z = "hand2"    #"mão"
