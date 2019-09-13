from tkinter import *

janela = Tk()

lb1 = Label(janela, text='Linha1', bg='white')
lb2 = Label(janela, text='Linha2', bg='yellow')
lb3 = Label(janela, text='Linha3', bg='blue')
lb4 = Label(janela, text='Linha4', bg='yellow')


lb1.pack(side=TOP, fill=BOTH, expand=1)#BOTH SIGNIFICA 'AMBOS'
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry('500x200+600+200')

janela.mainloop()
