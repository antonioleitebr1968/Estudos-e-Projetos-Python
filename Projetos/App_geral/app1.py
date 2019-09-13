from tkinter import *

class Conjuntoss(object):

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('CONJUNTOS')

        self.font = ('Verdana', 15, 'italic')

        logo = PhotoImage(file="imagens\\conjuntoss.gif")
        self.logo = Label(janela)
        self.logo["image"] = logo
        self.logo.image = logo
        self.logo.grid(row=0, column=0)

        self.f1 = Frame(janela, bg='#77B7F7')
        self.MostraElementos()

        self.lb1 = Label(janela, text="""Com base nos conjuntos 
A = {1, 2, 3}, 
B = {5, 6, 7} e 
C = {1, 2, 3, 4, 5, 6}, 
preencha os campos abaixo 
com a simbologia adequada:
{Pertence, não pertence, 
está contido e não está contido}""", fg="red", bg="yellow", font=self.font)
        self.lb1.grid(row=1, column=0, columnspan=2, sticky=W+E)

        self.lb2 = Label(self.f1, text="a) 3___A: ", font=self.font, fg="black", bg="#77B7F7")
        self.lb2.grid(row=0, column=0, sticky=W)

        self.ed2 = Entry(self.f1, font=self.font, fg='black')
        self.ed2.grid(row=0, column=1)

        self.lb3 = Label(self.f1, text="b) 7___C: ", font=self.font, fg="black", bg="#77B7F7")
        self.lb3.grid(row=1, column=0, sticky=W)

        self.ed3 = Entry(self.f1, font=self.font, fg='black')
        self.ed3.grid(row=1, column=1)

        self.lb4 = Label(self.f1, text="c) A___B: ", font=self.font, fg="black", bg="#77B7F7")
        self.lb4.grid(row=2, column=0, sticky=W)

        self.ed4 = Entry(self.f1, font=self.font, fg='black')
        self.ed4.grid(row=2, column=1)

        self.lb5 = Label(self.f1, text="d) B___C: ", font=self.font, fg="black", bg="#77B7F7")
        self.lb5.grid(row=3, column=0, sticky=W)

        self.ed5 = Entry(self.f1, font=self.font, fg='black')
        self.ed5.grid(row=3, column=1)

        self.lb6 = Label(self.f1, text="e) C___A: ", font=self.font, fg="black", bg="#77B7F7")
        self.lb6.grid(row=4, column=0, sticky=W)

        self.ed6 = Entry(self.f1, font=self.font, fg='black')
        self.ed6.grid(row=4, column=1)

        self.lb7 = Label(self.f1, text="f) C___B: ", font=self.font, fg="black", bg="#77B7F7")
        self.lb7.grid(row=5, column=0, sticky=W)

        self.ed7 = Entry(self.f1, font=self.font, fg='black')
        self.ed7.grid(row=5, column=1)

        self.bt1 = Button(self.f1, text='COMPLETAR', font=self.font, cursor='hand2', command=self.SomeElementos)
        self.bt1.grid(row=6, column=1)


    def Reiniciar(self):
        self.lb1.grid(row=1, column=0, columnspan=2, sticky=W + E)
        self.f1.grid(row=2, column=0, columnspan=2, sticky=W + E)
        self.lb.grid_forget()
        self.bt.grid_forget()


    def MostraElementos(self):
        self.f1.grid(row=2, column=0, columnspan=2, sticky=W + E)


    def SomeElementos(self):
        cont = 0
        self.font1 = ('Arial Black', 25, 'italic')
        self.f1.grid_forget()
        self.lb1.grid_forget()
        #Transformando
        a = self.ed2.get().lower()
        b = self.ed3.get().lower()
        c = self.ed4.get().lower()
        d = self.ed5.get().lower()
        e = self.ed6.get().lower()
        f = self.ed7.get().lower()
        if a == 'pertence':
            cont += 10
        if b == 'não pertence':
            cont += 10
        if c == 'não está contido':
            cont += 10
        if d == 'não está contido':
            cont += 10
        if e == 'não está contido':
            cont += 10
        if f == 'não está contido':
            cont += 10

        total = 60

        if cont == total:
            self.lb = Label(self.janela, text='PARABÉNS!!!\nVocê acertou todas!', fg='yellow', font=self.font1, bg='#77B7F7')
            self.lb.grid(row=1, column=0)
            self.bt = Button(self.janela, text='REINICIAR', font=self.font, cursor='hand2', command=self.Reiniciar)
            self.bt.grid(row=2, column=0)
        else:
            acertos = cont * 100 / total
            self.lb = Label(self.janela, text=f'Você obteve \n{acertos:.0f}% de acerto!', fg='yellow', font=self.font1, bg='#77B7F7')
            self.lb.grid(row=1, column=0)

            self.bt = Button(self.janela, text='REINICIAR', font=self.font, cursor='hand2', command=self.Reiniciar)
            self.bt.grid(row=2, column=0)


#eram os padrões
"""janela = Tk()
janela.title("Conjuntos")
#Conjuntoss(janela)
janela['bg'] = '#77B7F7'
janela.resizable(False, False)
janela.geometry("400x700+200+200")
janela.mainloop()"""
