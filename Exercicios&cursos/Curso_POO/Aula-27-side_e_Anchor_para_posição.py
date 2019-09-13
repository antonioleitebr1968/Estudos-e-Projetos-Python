from tkinter import *


i = Tk()
i.title('Programa financeiro')
i.geometry('800x600+250+30')
i.wm_iconbitmap('icone.ico')


lb1 = Label(i, text='label1', bg='yellow')
lb1.place(x=230, y=200)

lb2 = Label(i, text='label2', bg='red')
lb2.place(x=230, y=200)

lb3 = Label(i, text='label3', bg='blue')
lb3.place(x=230, y=200)

lb4 = Label(i, text='label4', bg='pink')
lb4.place(x=230, y=200)

lb1.pack(side=LEFT)
lb2.pack(side=RIGHT, anchor=NE)
lb3.pack(anchor=W)
lb4.pack(side=BOTTOM, anchor=CENTER)


i.mainloop()
