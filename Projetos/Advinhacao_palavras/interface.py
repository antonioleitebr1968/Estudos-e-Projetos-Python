import tkinter as tk
import cores_fontes as cf
from random import choice
from palavras import palavra_secreta
from functools import partial

class Interface(object):
    def __init__(self):
        self.__janela = tk.Tk()
        self.__janela.title('Jogo de Adivinhação')
        self.__janela.geometry('600x400+300+300')
        self.__janela['bg'] = cf.GOLD
        self.__janela.wm_iconbitmap('imgs\\war.ico')
        self.__janela.resizable(False, False)
        self.__acertos = 0

        self.__framePai = tk.Frame(self.__janela, bg=cf.GOLD, relief=tk.SUNKEN, bd=10)
        self.__framePai.pack(fill=tk.BOTH)


        self.__frameTop = tk.Frame(self.__framePai, bg=cf.GOLD)
        self.__frameTop.pack(fill=tk.BOTH)

        self.__letrasSaidas = []
        self.__palavraSecreta = choice(palavra_secreta)
        #print(self.__palavraSecreta)
        self.__descoberta = []
        self.__letra = ''
        self.__rodadas = len(self.__palavraSecreta) * 2

        self.criarWidgetsTop()
        self.lerEIniciar()
        self.chamarEventos()

        self.__janela.mainloop()

    def criarWidgetsTop(self):
        global configBt
        global entrada
        global palavraSecreta
        global textoLetras
        global rodadas
        global tentar

        configBt = {'font': cf.FONTE_VERDANA_BOLD, 'bg': 'white', 'fg': 'black',
                    'cursor': 'hand2', 'bd': 2, 'relief': tk.SOLID}
        configLabel = {'font': cf.FONTE_VERDANA_BOLD, 'bg': cf.GOLD}

        label = tk.Label(self.__frameTop, text='PALAVRA SECRETA', **configLabel)
        label.pack()

        palavraSecreta = tk.Label(self.__frameTop, text=f'{self.__descoberta}', **configLabel, height=2)
        palavraSecreta.pack()

        rodadas = tk.Label(self.__frameTop, text=f"Chance(s): {self.__rodadas}", **configLabel, pady=20)
        rodadas.pack()

        entrada = tk.Entry(self.__frameTop, font=cf.FONTE_VERDANA_BOLD, width=6)
        entrada.pack()
        entrada.focus_set()

        textoLetras = tk.Label(self.__frameTop, text='', **configLabel)
        textoLetras.pack()

        tentar = tk.Button(self.__frameTop, text='Tentar', **configBt, command=partial(self.tente, event=0))
        tentar.pack()

    def lerEIniciar(self):
        for i in range(0, len(self.__palavraSecreta)):
            self.__descoberta.append('-')

        palavra = ''.join(self.__descoberta)
        palavraSecreta['text'] = palavra

    def tente(self, event):
        if len(str(entrada.get())) > 0:
            self.__letra = str(entrada.get())[0].upper()
            if self.__letra not in self.__letrasSaidas:
                self.__letrasSaidas.append(self.__letra)
                textoLetras['text'] = ' '.join(self.__letrasSaidas)

            for i in range(0, len(self.__palavraSecreta)):
                if self.__letra == self.__palavraSecreta[i]:
                    self.__descoberta[i] = self.__letra
                    palavraSecreta['text'] = ''.join(self.__descoberta)

            if self.__descoberta == self.__palavraSecreta:
                self.__framePai.pack_forget()
                self.sucesso()

            self.__rodadas -= 1
            rodadas['text'] = f"Chance(s): {self.__rodadas}"

            if self.__rodadas == 0:
                self.__framePai.pack_forget()
                self.gameOver()

            entrada.delete(0, tk.END)

    def gameOver(self):
        global frameOver
        global btPerdeu

        frameOver = tk.Frame(self.__janela, bg=cf.GOLD)
        frameOver.pack(fill=tk.BOTH)

        labelperdeu = tk.Label(frameOver, text='GAME OVER CHAPA!', font=cf.FONTE_VERDANA_BOLD, bg=cf.GOLD)
        labelperdeu.pack()

        btPerdeu = tk.Button(frameOver, text='Reiniciar', command=partial(self.reiniciar, 1, event=0), **configBt)
        btPerdeu.pack()

        btPerdeu.bind('<Enter>', partial(self.configurarBt, btPerdeu, 5))
        btPerdeu.bind('<Leave>', partial(self.configurarBt, btPerdeu, 2))

        btPerdeu.focus_set()
        btPerdeu.bind('<Return>', partial(self.reiniciar, 1))

    def reiniciar(self, op, event):
        if op == 1:
            frameOver.pack_forget()
        else:
            frameSucess.pack_forget()

        self.__framePai.pack(fill=tk.BOTH)
        self.__rodadas = len(self.__palavraSecreta) * 2
        self.__letrasSaidas = []
        self.__palavraSecreta = choice(palavra_secreta)
        self.__descoberta = []
        self.__letra = ''
        self.lerEIniciar()
        textoLetras['text'] = ''
        self.__rodadas = len(self.__palavraSecreta) * 2
        rodadas['text'] = f"Chance(s): {self.__rodadas}"
        entrada.focus_set()

    def sucesso(self):
        global frameSucess
        global btSucess

        frameSucess = tk.Frame(self.__janela, bg=cf.GOLD)
        frameSucess.pack(fill=tk.BOTH)

        labelSucess = tk.Label(frameSucess, text=f'ACERTO MIZERAVI! \nPALAVRA: {"".join(self.__descoberta)}', font=cf.FONTE_VERDANA_BOLD, bg=cf.GOLD)
        labelSucess.pack()

        btSucess = tk.Button(frameSucess, text='Reiniciar', command=partial(self.reiniciar, 0, event=0), **configBt)
        btSucess.pack()

        btSucess.bind('<Enter>', partial(self.configurarBt, btSucess, 5))
        btSucess.bind('<Leave>', partial(self.configurarBt, btSucess, 2))

        btSucess.focus_set()
        btSucess.bind('<Return>', partial(self.reiniciar, 0))

    def chamarEventos(self):
        tentar.bind('<Enter>', partial(self.configurarBt, tentar, 5))
        tentar.bind('<Leave>', partial(self.configurarBt, tentar, 2))
        entrada.bind('<Return>', self.tente)
        tentar.bind('<Return>', self.tente)

    def configurarBt(self, obj, bd, event):
        obj.configure(bd=bd)

if __name__ == '__main__':
    Interface()
