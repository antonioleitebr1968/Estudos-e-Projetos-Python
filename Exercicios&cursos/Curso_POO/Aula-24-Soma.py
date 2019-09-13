from tkinter import *

def bt_click():
    if (str(ed1.get())).isnumeric() and (str(ed1.get())).isnumeric():
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1 + num2
    else:
        lb['text'] = 'Os valores são inválidos'
        lb['bg'] = 'red'
def bt_click2():
    if (str(ed1.get())).isnumeric() and (str(ed1.get())).isnumeric():
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1 * num2
    else:
        lb['text'] = 'Os valores são inválidos'
        lb['bg'] = 'red'
i = Tk()
i.title('Programa financeiro')
i.geometry('800x600+250+30')
i.wm_iconbitmap('icone.ico')
lb = Label(i, text='0', bg='yellow')
lb.place(x=230, y=200)

bt = Button(i, width='20', text='Somar', command=bt_click)
bt.place(x=230, y=230)

bt = Button(i, width='20', text='Multiplicar', command=bt_click2)
bt.place(x=230, y=260)

ed1 = Entry(i)# componente input
ed1.place(x=230, y=150)#posição

ed2 = Entry(i)# componente input
ed2.place(x=230, y=180)#posição


ed1.pack()
ed2.pack()
lb.pack()
bt.pack()

i.mainloop()