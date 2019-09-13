from tkinter import *

class TesteLogin:
    def __init__(self, janela):
        # logo do aplicativo
        logo = PhotoImage(file = 'C:\\Users\\user\\Pictures\\PythonLogo.gif')#caminho da gif
        self.logo = Label(janela)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        self.frameSupremo = Frame(janela, bg='green')
        self.frameSupremo.pack()

        #criando fonte
        self.font = ('Verdana', 15, 'italic')
        # Criando Frames
        self.frame1 = Frame(self.frameSupremo, pady=5, bg='green')
        self.frame2 = Frame(self.frameSupremo, pady=15,padx=15, bg='#1BFEF2')
        self.frame3 = Frame(self.frameSupremo, pady=5, bg='green')
        self.frame4 = Frame(self.frameSupremo, pady=15, padx=15, bg='#1BFEF2')
        self.frame5 = Frame(self.frameSupremo, pady=5, bg='green')
        self.frame6 = Frame(self.frameSupremo, pady=5, bg='green')
        # Empacotando Frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()


        self.lb1 = Label(self.frame1, text='Login', font= self.font, fg='#1BFEF2', bg='green')
        self.lb1.pack()

        self.ed1 = Entry(self.frame2, width=20, font=self.font)
        self.ed1.pack()

        self.lb2 = Label(self.frame3, text='Senha', font= self.font, fg='#1BFEF2', bg='green')
        self.lb2.pack()

        self.ed2 = Entry(self.frame4, width=20, show='*', font=self.font)
        self.ed2.pack()

        #botão especial
        but = PhotoImage(file='C:\\Users\\user\\Pictures\\clique.ppm')  # caminho da gif
        self.but = Button(self.frame6, cursor='hand2',command=self.logando)
        self.but['image'] = but
        self.but.image = but
        self.but.pack()

        """self.bt1 = Button(self.frame5, text='clicar', fg='black', width=15, command=self.logando, font= self.font, bg='#1BFEF2')
        self.bt1.pack()"""

        self.resp = Label(self.frame6, text='', font= self.font, bg='green')
        self.resp.pack()

    def logando(self):
        a = self.ed1.get()
        result = a.capitalize()
        if result == 'Matheus' and self.ed2.get() == '1401':
            self.resp['text'] = f'Bem vindo {result}'
            self.resp['bg'] = 'green'
            self.resp['fg'] = 'blue'
            self.resp['font'] = 'Vijaya', 25, 'bold'
        else:
            self.resp['text'] = 'Loguin ou senha incorretos'
            self.resp['bg'] = 'green'
            self.resp['fg'] = 'yellow'
            self.resp['font'] = 'Vijaya', 25, 'bold'

janela = Tk()
TesteLogin(janela)
janela.title('LOGIN...')
janela.wm_iconbitmap('testeloguin.ico')
#definindo cor de background
janela['bg'] = '#77B7F7'
janela.geometry('600x600+200+200')
janela.mainloop()
