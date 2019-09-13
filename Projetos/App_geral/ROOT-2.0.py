from pylab import *
from tkinter import *
from app1 import Conjuntoss
from app2 import desenhar
from app3 import Projeto

class root:

    def __init__(self):
        self.font = ('Verdana', 34, 'bold')
        self.font2 = ('Verdana', 20, 'bold')

        self.janela = Tk()
        self.janela.title('App Geral')
        #self.janela.wm_iconbitmap('imagens\\g1.ico')
        self.janela.resizable(False, False)
        self.janela.geometry('1280x720+200+200')
        self.janela['bg'] = '#48D1CC'

        #frame superior para conter a logo
        self.frameSup = Frame(self.janela, bg='#48D1CC', padx=110)
        self.frameSup.grid(row=0, column=0)

        logo = PhotoImage(file="imagens\\g5.gif")
        self.logo = Label(self.frameSup)
        self.logo["image"] = logo
        self.logo.image = logo
        self.logo.grid(row=0, column=0)

        self.lb1 = Label(self.janela, text='Usuário', font=self.font, bg='#48D1CC', fg='#687171', pady=20)
        self.lb1.grid(row=1, column=0)

        self.ed1 = Entry(self.janela, fg='#48D1CC', font=self.font)
        self.ed1.grid(row=2, column=0)

        self.lb2 = Label(self.janela, text='Senha', font=self.font, bg='#48D1CC', fg='#687171', pady=20)
        self.lb2.grid(row=3, column=0)

        self.ed2 = Entry(self.janela, fg='#48D1CC', font=self.font, show='*')
        self.ed2.grid(row=4, column=0)

        #criando botão
        self.fs = Frame(self.janela, pady=10, bg='#48D1CC')
        self.fs.grid(row=5, column=0)
        but = PhotoImage(file='imagens\\g6.gif')# caminho da gif
        self.but = Button(self.fs, cursor='hand2', pady=50, bd=2, command=self.verificar)
        self.but.focus_force()#força o foco no botão
        self.but.bind('<Return>', self.verificar)#pega o botão Enter e associa a função
        self.but['image'] = but
        self.but.image = but
        self.but.grid()

        self.lb3 = Label(self.janela, text='', fg='yellow', bg='#48D1CC')
        self.lb3['font'] = self.font
        self.lb3.grid(row=6, column=0)


        self.janela.mainloop()

    def verificar(self, event = 0): # O 'Event' é preciso para que a entrada do botão funcione
        a, b = str(self.ed1.get()), str(self.ed2.get())
        if a != 'matheus' or b != 'mm1401':
            self.lb3['text'] = 'Senha ou usuário incorreto.'
        else:
            if a == 'matheus' and b == 'mm1401':
                print('entrou')
                self.forgetTela1()
                self.mostraTela2()


    def forgetTela1(self):
        self.frameSup.grid_forget()
        self.lb1.grid_forget()
        self.ed1.grid_forget()
        self.lb2.grid_forget()
        self.ed2.grid_forget()
        self.fs.grid_forget()
        self.lb3.grid_forget()


    def mostraTela2(self):
        # botão voltar ============================================================
        self.f1 = Frame(self.janela, pady=20, bg='#48D1CC')
        #self.f1.pack(side=LEFT, anchor=NW)
        self.f1.grid(row=0, column=0, sticky=NW)
        but = PhotoImage(file='imagens\\back.gif')  # caminho da gif
        self.but1 = Button(self.f1, cursor='hand2', command=self.voltar, bd=2)
        self.but1['image'] = but
        self.but1.image = but
        #self.but1.pack()
        self.but1.grid()
        #==========================================================================

        self.f2 = Frame(self.janela, pady=10, bg='#48D1CC')
        #self.f2.pack()
        self.f2.grid(row=2, column=0)
        self.but2 = Button(self.f2, cursor='hand2', bd=0, text='Conjuntos com interface', font=self.font2, command=self.chamaApp1, width=70)
        self.but2['bg'] = '#687171'
        self.but2['fg'] = '#48D1CC'
        #self.but2.pack()
        self.but2.grid()

        self.f3 = Frame(self.janela, pady=10, bg='#48D1CC')
        #self.f3.pack()
        self.f3.grid(row=3, column=0)
        self.but3 = Button(self.f3, cursor='hand2', bd=0, text='Desenhar', font=self.font2, command=self.chamaApp2, width=70)
        self.but3['bg'] = '#687171'
        self.but3['fg'] = '#48D1CC'
        #self.but3.pack()
        self.but3.grid()

        self.f4 = Frame(self.janela, pady=10, bg='#48D1CC')
        # self.f3.pack()
        self.f4.grid(row=4, column=0)
        self.but4 = Button(self.f4, cursor='hand2', bd=0, text='Inovação tecnológica e empreendedorismo', font=self.font2, command=self.chamaApp3, width=70)
        self.but4['bg'] = '#687171'
        self.but4['fg'] = '#48D1CC'
        # self.but3.pack()
        self.but4.grid()



    def chamaApp1(self):
        #self.f1.pack_forget()
        #self.f2.pack_forget()
        #self.f3.pack_forget()
        self.f1.grid_forget()
        self.f2.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.janela['bg'] = '#77B7F7'
        self.janela.geometry("400x700+200+200")
        Conjuntoss(self.janela)


    def voltar(self):
        self.frameSup.grid(row=0, column=0)
        self.lb1.grid(row=1, column=0)
        self.ed1.grid(row=2, column=0)
        self.lb2.grid(row=3, column=0)
        self.ed2.grid(row=4, column=0)
        self.fs.grid(row=5, column=0)
        #self.f1.pack_forget()
        #self.f2.pack_forget()
        #self.f3.pack_forget()
        self.f1.grid_forget()
        self.f2.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()

    def chamaApp2(self):
        #self.f1.pack_forget()
        #self.f2.pack_forget()
        #self.f3.pack_forget()
        self.f1.grid_forget()
        self.f2.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
        self.janela.geometry(f'900x900+200+200')
        self.janela['bg'] = '#77B7F7'
        desenhar(self.janela)


    def chamaApp3(self):
        self.f1.grid_forget()
        self.f2.grid_forget()
        self.f3.grid_forget()
        self.f4.grid_forget()
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
        self.janela.resizable(False, False)
        self.janela.geometry('1200x700+100+100')
        self.janela['bg'] = self.PASTEL
        Projeto(self.janela)
root()
