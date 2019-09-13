#TELA DE LOGIN E SENHA

from tkinter import *

janela = Tk()

lb1 = Label(janela, text="Login: ")#criando label
lb2 = Label(janela, text="Senha: ")

ed1 = Entry(janela)#criando o "input"
ed2 = Entry(janela)

bt1 = Button(janela, text="Confirmar")#criando botão
#Abaixo: definindo gerenciadores de leiute

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=1)

janela.geometry("200x100+100+100")

janela.mainloop()
