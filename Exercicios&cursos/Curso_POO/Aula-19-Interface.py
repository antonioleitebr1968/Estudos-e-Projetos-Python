from tkinter import *

def bt_click():
    lb['text'] = 'Trocou o texto'# definindo o botão

def bt_clicar():
    print(ed.get())
    lb['text'] = ed.get()

i = Tk()
i.title('Programa financeiro')
i.geometry('800x600+250+30')# criando janela
i.wm_iconbitmap('icone.ico')# colocando icone na janela
#i['bg'] = 'black' # definindo a cor de fundo da janela

lb = Label(i, text='Matheus Morais')# criando um label(um texto)
lb.place(x=100, y=100)

bt = Button(i, width='20', text='Ok', command=bt_click)# criando um botão
bt.place(x=230, y=100)

bt = Button(i, width='20', text='Capturar', command=bt_clicar)
bt.place(x=230, y=190)

ed = Entry(i)# componente input
ed.place(x=230, y=150)#posição


i.mainloop()
