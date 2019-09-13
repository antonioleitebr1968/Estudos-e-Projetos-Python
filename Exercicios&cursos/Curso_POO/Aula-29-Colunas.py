from tkinter import *


i = Tk()
i.title('Programa financeiro')
i.geometry('200x120+350+100')
i.wm_iconbitmap('icone.ico')

lb3 = Label(i, text='', width=5, height=2)
lb3.grid(row=0, column=0)


lb1 = Label(i, text='Login')
lb1.grid(row=1, column=1)

lb2 = Label(i, text='Senha')
lb2.grid(row=2, column=1)


ed1 = Entry(i)
ed1.grid(row=1, column=2)

ed2 = Entry(i)
ed2.grid(row=2, column=2)

bt1 = Button(i, text='Login')
bt1.grid(row=3, column=2)


i.mainloop()
