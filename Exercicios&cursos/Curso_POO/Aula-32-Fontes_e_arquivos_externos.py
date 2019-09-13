from tkinter import *
from constantes import *

i = Tk()
i.title('Programa financeiro')
i.geometry(f'{LARGURA}x{ALTURA}')
i.wm_iconbitmap('icone.ico')

lb1 = Label(i, text='ESPAÇAMENTO', width=15, height=3, bg='red', font="Verdana, 10 bold")
lbh = Label(i, text='HORIZONTAL', bg='blue')
lbv = Label(i, text='VERTICAL', bg='yellow')

lb1.grid(row=0, column=0)
lbh.grid(row=1, column=0, sticky=E)
lbv.grid(row=0, column=1, sticky=N)

i.mainloop()
