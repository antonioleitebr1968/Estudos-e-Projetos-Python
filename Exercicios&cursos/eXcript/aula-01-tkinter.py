#OBS: toda janela é também um dicionario
import tkinter

janela = tkinter.Tk()# janela principal

janela.title('Janela principal')# definindo o titulo da janela

janela['bg'] = 'green'# definindo cor da janela

#---------------------------------------------------------------
#Largura x Altura + esquerda do video + topo do video
# exemplo: 300 x 300 + 100 + 100
janela.geometry('800x800+100+100')# definindo dimensão da janela
#janela.geometry('800x800')# outra forma de definir, porem a janela é criada em qualquer lugar do video
#janela.geometry('+100+100') #definindo apenas esquerda e topo
#---------------------------------------------------------------
#OBS: o tkinter manipula todos os valores como sendo pixels
janela.mainloop()# referencia a janela principal/essa função é um loopin
