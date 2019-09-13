from tkinter import *

def bt1_click():
    lb2 = Label(janela, text='Ah! Olá senhor ')
    lb2.grid(row=2, column=1)
    lb3 = Label(janela, text='')
    lb3.grid(row=3, column=1)
    lb3['text'] = ed1.get() + '!!'

janela = Tk()

lb1 = Label(janela, text="Qual o seu nome? ", bg='green')
lb1.grid(row=0, column=0)

ed1 = Entry(janela)
ed1.grid(row=0, column=1)

bt1 = Button(janela, text='Enter', width=5, height=1, comman=bt1_click)
bt1.grid(row=1, column=1)


janela.geometry('300x200+500+500')
janela.mainloop()
