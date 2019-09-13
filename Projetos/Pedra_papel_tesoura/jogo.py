import tkinter as tk
import cores_fontes as cf
import random
from functools import partial
import time

class Tela(object):
    def __init__(self):

        self.__janela = tk.Tk()
        self.__janela.title('Pedra Papel Tesoura')
        self.__janela.resizable(False, False)
        self.__janela.geometry('700x600+200+200')
        self.__janela['bg'] = cf.PASTEL
        self.__janela.wm_iconbitmap('imgs\\icone.ico')

        self.__caminho_pedra = tk.PhotoImage(file="imgs\\pedra.png")
        self.__caminho_papel = tk.PhotoImage(file="imgs\\papel.png")
        self.__caminho_tesoura = tk.PhotoImage(file="imgs\\tesoura.png")

        self.__jogada_player = 0

        self.__contador_player = 0
        self.__contador_pc = 0

        self.__vencendo = 0

        self.__criar_widgets()
        self.rodar()

    def rodar(self):
        self.__janela.mainloop()

    def __criar_widgets(self):
        # dicionarios de configurações =================================================================================
        self.__config_text_jogador = {'text': 'jogador:', 'font': cf.FONTE_BAUSHAUS_93_BOLD, 'padx': 30,
                                    'bg': cf.PASTEL}
        self.__config_text_jogador_pontuacao = {'font': cf.FONTE_BAUSHAUS_93_BOLD,
                                              'bg': cf.PASTEL}

        self.__config_text_computador = {'text': 'computador:', 'font': cf.FONTE_BAUSHAUS_93_BOLD, 'padx': 10,
                                       'bg': cf.PASTEL}
        self.__config_text_computador_pontuacao = {'font': cf.FONTE_BAUSHAUS_93_BOLD,
                                                 'bg': cf.PASTEL}
        self.__config_frame_lados = {'width': 220, 'height': 250, 'bd': 8, 'relief': tk.SUNKEN}
        # ==============================================================================================================

        # ==============frames principais===============================================================================
        self.__frame_pai = tk.Frame(self.__janela, bg=cf.PASTEL)
        self.__frame_pai.pack(fill=tk.X)

        self.__frame_topo = tk.Frame(self.__frame_pai, bg=cf.PASTEL, pady=20)
        self.__frame_topo.pack(fill=tk.X)

        self.__frame_central = tk.Frame(self.__frame_pai, bg=cf.PASTEL)
        self.__frame_central.pack(fill=tk.X)

        self.__frame_inferior = tk.Frame(self.__frame_pai, bg=cf.PASTEL, pady=30)
        self.__frame_inferior.pack()

        # ==============================================================================================================

        # ==============================================================================================================
        self.__frame_jogador = tk.Frame(self.__frame_topo, bg=cf.PASTEL)
        self.__frame_jogador.pack(side=tk.LEFT, anchor=tk.NW)

        self.__frame_computador = tk.Frame(self.__frame_topo, bg=cf.PASTEL)
        self.__frame_computador.pack(side=tk.RIGHT, anchor=tk.NE)

        self.__text_jogador = tk.Label(self.__frame_jogador, **self.__config_text_jogador)
        self.__text_jogador.grid(row=0, column=0)

        self.__text_jogador_pontuacao = tk.Label(self.__frame_jogador, **self.__config_text_jogador_pontuacao,
                                                 text='0')
        self.__text_jogador_pontuacao.grid(row=1, column=0)

        self.__text_computador = tk.Label(self.__frame_computador, **self.__config_text_computador)
        self.__text_computador.grid(row=0, column=0)

        self.__text_computador_pontuacao = tk.Label(self.__frame_computador, **self.__config_text_computador_pontuacao,
                                                    text='0')
        self.__text_computador_pontuacao.grid(row=1, column=0)
        # ==============================================================================================================

        # ==============================================================================================================
        self.__lado_computador = tk.Frame(self.__frame_central, **self.__config_frame_lados)
        self.__lado_computador.pack(side=tk.RIGHT, anchor=tk.NE)

        self.__img_computador = tk.PhotoImage(file="imgs\\pc.png")
        self.__label_img_computador = tk.Label(self.__lado_computador, image=self.__img_computador,
                                               width=220, height=250)
        self.__label_img_computador.pack()

        self.__versos = tk.Label(self.__janela, text='X', font=cf.FONTE_BAUSHAUS_93_BOLD_EXTRA_GRANDE, bg=cf.PASTEL)
        self.__versos.place(x=330, y=220)

        self.__lado_jogador = tk.Frame(self.__frame_central, **self.__config_frame_lados)
        self.__lado_jogador.pack(side=tk.LEFT, anchor=tk.NW)

        self.__img_jogador = tk.PhotoImage(file="imgs\\player.png")
        self.__label_img_jogador = tk.Label(self.__lado_jogador, image=self.__img_jogador, width=220, height=250,
                                            bg='white')
        self.__label_img_jogador.pack()

        # ==============================================================================================================

        # ==============================================================================================================

        self.__botao_pedra = tk.Button(self.__frame_inferior, text='Pedra', font=cf.FONTE_BAUSHAUS_93_BOLD, width=8,
                                     cursor='hand2', bd=5, relief=tk.RIDGE, command=self.__pedra)
        self.__botao_pedra.grid(row=0, column=0)

        self.__botao_papel = tk.Button(self.__frame_inferior, text='Papel', font=cf.FONTE_BAUSHAUS_93_BOLD, width=8,
                                     cursor='hand2', bd=5, relief=tk.RIDGE, command=self.__papel)
        self.__botao_papel.grid(row=0, column=1)

        self.__botao_tesoura = tk.Button(self.__frame_inferior, text='Tesoura', font=cf.FONTE_BAUSHAUS_93_BOLD, width=8,
                                       cursor='hand2', bd=5, relief=tk.RIDGE, command=self.__tesoura)
        self.__botao_tesoura.grid(row=0, column=2)
        # ==============================================================================================================


    def __escolher_img_computador(self, referencia):
        self.__img_computador['image'] = referencia

    def __pedra(self):
        self.__att = tk.PhotoImage(file="imgs\\pedra.png")
        self.__label_img_jogador['image'] = self.__att
        self.__jogada_player = 1
        self.__embate()

    def __papel(self):
        self.__att = tk.PhotoImage(file="imgs\\papel.png")
        self.__label_img_jogador['image'] = self.__att
        self.__jogada_player = 2
        self.__embate()

    def __tesoura(self):
        self.__att = tk.PhotoImage(file="imgs\\tesoura.png")
        self.__label_img_jogador['image'] = self.__att
        self.__jogada_player = 3
        self.__embate()

    def __pc_joga(self):
        self.__pc = random.randint(1, 3)
        if self.__pc == 1:
            self.__label_img_computador.configure(image=self.__caminho_pedra)
        elif self.__pc == 2:
            self.__label_img_computador.configure(image=self.__caminho_papel)
        else:
            self.__label_img_computador.configure(image=self.__caminho_tesoura)

        return self.__pc

    def __embate(self):
        self.__jogada_pc = self.__pc_joga()
        if self.__jogada_player == 1 and self.__jogada_pc == 3:
            self.__contador_player += 1
            self.__text_jogador_pontuacao['text'] = str(self.__contador_player)

        elif self.__jogada_player == 2 and self.__jogada_pc == 1:
            self.__contador_player += 1
            self.__text_jogador_pontuacao['text'] = str(self.__contador_player)

        elif self.__jogada_player == 3 and self.__jogada_pc == 2:
            self.__contador_player += 1
            self.__text_jogador_pontuacao['text'] = str(self.__contador_player)

        elif self.__jogada_pc == 1 and self.__jogada_player == 3:
            self.__contador_pc += 1
            self.__text_computador_pontuacao['text'] = str(self.__contador_pc)

        elif self.__jogada_pc == 2 and self.__jogada_player == 1:
            self.__contador_pc += 1
            self.__text_computador_pontuacao['text'] = str(self.__contador_pc)

        elif self.__jogada_pc == 3 and self.__jogada_player == 2:
            self.__contador_pc += 1
            self.__text_computador_pontuacao['text'] = str(self.__contador_pc)

        self.__verifica_quem_esta_vencendo()


    def __verifica_quem_esta_vencendo(self):
        if self.__contador_player > self.__contador_pc:
            self.__text_jogador_pontuacao['fg'] = 'green'
            self.__text_computador_pontuacao['fg'] = cf.VERMELHO
        elif self.__contador_player < self.__contador_pc:
            self.__text_jogador_pontuacao['fg'] = cf.VERMELHO
            self.__text_computador_pontuacao['fg'] = 'green'
        else:
            self.__text_jogador_pontuacao['fg'] = 'black'
            self.__text_computador_pontuacao['fg'] = 'black'

if __name__ == '__main__':
    Tela()
