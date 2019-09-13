from tkinter import *

janela = Tk()

lb1 = Label(janela, text='label1', bg='green')
lb2 = Label(janela, text='label2', bg='red')
lb3 = Label(janela, text='label3', bg='yellow')
lb4 = Label(janela, text='label4', bg='blue')

lb2.pack()
lb1.pack()
lb3.pack()
lb4.pack(side=BOTTOM)





janela.geometry('400x300+200+200')
janela.mainloop()

#Nota: Propriedade SIDE
#TOP == TOPO
#LEFT == ESQUERDA
#RIGHT == DIREITA
#BOTTOM == INFERIOR