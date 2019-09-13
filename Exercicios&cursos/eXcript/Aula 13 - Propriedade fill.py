#obs: x é horizontal e y é vertical
from tkinter import *

janela = Tk()

lb1 = Label(janela, text='horizontal', bg='white')
lb2 = Label(janela, text='2', bg='black')
lb3 = Label(janela, text='3', bg='black')


lb1.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)


janela.geometry('500x200+600+200')

janela.mainloop()
