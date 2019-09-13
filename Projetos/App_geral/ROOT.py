from tkinter import *
from app1 import Conjuntoss

class root:

    def __init__(self):
        self.font = ('Verdana', 34, 'bold')

        self.janela = Tk()
        self.janela.title('App Geral')
        self.janela.wm_iconbitmap('imagens\\g1.ico')
        #self.janela.resizable(False, False)
        self.janela.geometry('1220x720+200+200')
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

        self.ed1= Entry(self.janela, fg='#48D1CC', font=self.font)
        self.ed1.grid(row=2, column=0)

        self.lb2 = Label(self.janela, text='Senha', font=self.font, bg='#48D1CC', fg='#687171', pady=20)
        self.lb2.grid(row=3, column=0)

        self.ed2 = Entry(self.janela, fg='#48D1CC', font=self.font, show='*')
        self.ed2.grid(row=4, column=0)

        #criando botão
        self.fs = Frame(self.janela, pady=10, bg='#48D1CC')
        self.fs.grid(row=5, column=0)
        but = PhotoImage(file='imagens\\g6.gif')# caminho da gif
        self.but = Button(self.fs, cursor='hand2', pady=50, command=self.logarOUnao, bd=2)
        self.but['image'] = but
        self.but.image = but
        self.but.grid()


        self.janela.mainloop()

    def sometudo(self):
        self.but1.grid_forget()
        self.but2.grid_forget()
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
        self.but1.grid_forget()
        self.but2.grid_forget()


    def prosseguir(self):
        self.frameSup.grid_forget()
        self.lb1.grid_forget()
        self.ed1.grid_forget()
        self.lb2.grid_forget()
        self.ed2.grid_forget()
        self.fs.grid_forget()

        but = PhotoImage(file='imagens\\back.gif')  # caminho da gif
        self.but1 = Button(self.janela, cursor='hand2', pady=50, command=self.voltar, bd=2)
        self.but1['image'] = but
        self.but1.image = but

        self.but2 = Button(self.janela, cursor='hand2', bd=0, text='Conjuntos com interface', font=self.font, padx=300, command=self.sometudo)
        self.but2['bg'] = '#687171'
        self.but2['fg'] = '#48D1CC'


    def logarOUnao(self):
        a, b = str(self.ed1.get()), str(self.ed2.get())
        if a != 'matheus' and b != 'mm1401':
            self.lbb = Label(self.janela, text='Senha ou usuário incorreto.', fg='yellow', bg='#48D1CC')
            self.lbb['font'] = self.font
            self.lbb.grid(row=6, column=0)
        else:
            if a == 'matheus' and b == 'mm1401':
                self.prosseguir()
                self.mostraELementos()
                if self.lbb in self.janela:
                    self.lbb.grid_forget()

    def mostraELementos(self):
        self.but1.grid(row=0, column=0, sticky=NW)
        self.but2.grid(row=1, column=0)

root()

