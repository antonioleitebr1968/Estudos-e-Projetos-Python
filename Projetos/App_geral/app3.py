from pylab import *
from tkinter import *

class Projeto():

    def __init__(self, janela):#aqui entra a variável de inicialização no ROOT 2.0

        #############VARIÁVEIS CONTENDO CORES##################
        self.AZUL = '#48D1CC'
        self.CINZA = '#A9A9A9'
        self.ROXO = '#6A5ACD'
        self.ROSA = '#FF69B4'
        self.AZUL_CLARIN = '#00BFFF'
        self.AZUL_CLARO_DA_PESTE = '#87CEFA'
        self.VERMELHO = '#A52A2A'
        self.VERDE_CLARO = '#00FF00'
        self.SEI_LA = '#FFDEAD'
        self.LARANJA = '#FF8C00'
        self.AZUL_CINZA = '#B0C4DE'
        self.PASTEL = '#E6E6FA'
        #######################################################

        self.janela = janela
        self.janela.title('PROJETO')
        self.janela.wm_iconbitmap('img\\icone.ico')

        self.font = ('Verdana', 15, 'italic')
        self.font2 = ('Impact', 20, 'bold')

        #criando label de boas vindas
        self.label_boas_vindas = Label(self.janela, text='Olá pessoal, boa noite a todos! :)', bg=self.ROXO)
        self.label_boas_vindas['padx'] = 230
        self.label_boas_vindas['fg'] = 'white'
        self.label_boas_vindas['font'] = self.font

        self.label_titulo = Label(self.janela, text='Inovação tecnológica e empreendedorismo', bg=self.ROXO)
        self.label_titulo['padx'] = 230
        self.label_titulo['fg'] = 'white'
        self.label_titulo['font'] = self.font2



        #img inicial----------------------------------------------------
        self.frame_img_inicial = Frame(self.janela, bg=self.PASTEL)
        img_inicial = PhotoImage(file="img\\Inteligência-Artificial.png")
        self.img_inicial = Label(self.frame_img_inicial)
        self.img_inicial["image"] = img_inicial
        self.img_inicial.image = img_inicial
        self.img_inicial.pack()
        #---------------------------------------------------------------

        #BOTÃO----------------------------------------------------------------------------------------------
        #self.frame_botao = Frame(self.janela, pady=10, bg=self.ROXO)
        self.botao_inicial = Button(self.janela, text='Avançar', font=self.font2, cursor='hand2', pady=10)
        self.botao_inicial['padx'] = 40
        self.botao_inicial['bd'] = 5
        self.botao_inicial['bg'] = self.PASTEL
        self.botao_inicial['fg'] = self.ROXO
        self.botao_inicial['command'] = self.ESCONDE_ELEMENTOS_TELA_INICIAL
        #self.botao_inicial['width'] = 70
        #---------------------------------------------------------------------------------------------------

        self.MOSTRA_ELEMENTOS_TELA_INICIAL()
        self.janela.mainloop()

#####FUNÇÕES########################################################################################
    def mostrarImagemInicial(self):
        self.frame_img_inicial.pack(fill=X)

    def mostrarLabelsiniciais(self):
        self.label_boas_vindas.pack(fill=X)
        self.label_titulo.pack(fill=X)

    def ByMatheusMorais(self):
        self.font3 = ('Vijaya', 20, 'italic')
        self.identi_ficacao = Label(self.janela, text='By: Matheus Morais', fg=self.ROXO)
        self.identi_ficacao['font'] = self.font3
        self.identi_ficacao['bg'] = self.PASTEL
        self.identi_ficacao.pack(side=BOTTOM, anchor=SW)

    def botaoProsseguir(self):
        self.botao_inicial.pack(side=BOTTOM, fill=X)


    def MOSTRA_ELEMENTOS_TELA_INICIAL(self):
        self.mostrarLabelsiniciais()
        self.mostrarImagemInicial()
        self.ByMatheusMorais()
        self.botaoProsseguir()

    def ESCONDE_ELEMENTOS_TELA_INICIAL(self):
        self.janela.geometry('800x700+100+100')
        self.Gerar_Grafico()
        self.label_boas_vindas.pack_forget()
        self.frame_img_inicial.pack_forget()
        self.botao_inicial.pack_forget()


    def Gerar_Grafico(self):
        ###################################################################################
        self.Frame_esquerdo = Frame(self.janela, bg=self.PASTEL, pady=5)
        self.Frame_esquerdo.pack()
        self.lb1 = Label(self.Frame_esquerdo, text='Janeiro: ',font=self.font, bg=self.PASTEL)
        self.lb1['fg'] = self.ROXO
        self.lb1['font'] = self.font2
        self.lb1.grid(row=0, column=0)
        self.ed1 = Entry(self.Frame_esquerdo, fg=self.ROXO, font=self.font)
        self.ed1.grid(row=0, column=1)
        ####################################################################################

        ###################################################################################
        self.lb2 = Label(self.Frame_esquerdo, text='Fevereiro: ', font=self.font, bg=self.PASTEL)
        self.lb2['fg'] = self.ROXO
        self.lb2['font'] = self.font2
        self.lb2.grid(row=1, column=0)
        self.ed2 = Entry(self.Frame_esquerdo, fg=self.ROXO, font=self.font)
        self.ed2.grid(row=1, column=1)
        ####################################################################################

        ###################################################################################

        self.lb3= Label(self.Frame_esquerdo, text='Março: ', font=self.font, bg=self.PASTEL)
        self.lb3['fg'] = self.ROXO
        self.lb3['font'] = self.font2
        self.lb3.grid(row=2, column=0)
        self.ed3 = Entry(self.Frame_esquerdo, fg=self.ROXO, font=self.font)
        self.ed3.grid(row=2, column=1)
        ####################################################################################

        ###################################################################################

        self.lb4 = Label(self.Frame_esquerdo, text='Abril: ', font=self.font, bg=self.PASTEL)
        self.lb4['fg'] = self.ROXO
        self.lb4['font'] = self.font2
        self.lb4.grid(row=3, column=0)
        self.ed4 = Entry(self.Frame_esquerdo, fg=self.ROXO, font=self.font)
        self.ed4.grid(row=3, column=1)
        ####################################################################################

        ###################################################################################

        self.lb5 = Label(self.Frame_esquerdo, text='Maio: ', font=self.font, bg=self.PASTEL)
        self.lb5['fg'] = self.ROXO
        self.lb5['font'] = self.font2
        self.lb5.grid(row=4, column=0)
        self.ed5 = Entry(self.Frame_esquerdo, fg=self.ROXO, font=self.font)
        self.ed5.grid(row=4, column=1)
        ####################################################################################

        ###################################################################################

        self.lb6 = Label(self.Frame_esquerdo, text='Junho: ', font=self.font, bg=self.PASTEL)
        self.lb6['fg'] = self.ROXO
        self.lb6['font'] = self.font2
        self.lb6.grid(row=5, column=0)
        self.ed6 = Entry(self.Frame_esquerdo, fg=self.ROXO, font=self.font)
        self.ed6.grid(row=5, column=1)
        ####################################################################################

        ###################################################################################
        self.frame_direito = Frame(self.janela, bg=self.PASTEL, pady=5)
        self.frame_direito.pack()
        self.lb7 = Label(self.frame_direito, text='Julho: ', font=self.font, bg=self.PASTEL)
        self.lb7['fg'] = self.ROXO
        self.lb7['font'] = self.font2
        self.lb7.grid(row=6, column=0)
        self.ed7 = Entry(self.frame_direito, fg=self.ROXO, font=self.font)
        self.ed7.grid(row=6, column=1)
        ####################################################################################

        ###################################################################################

        self.lb8 = Label(self.frame_direito, text='Agosto: ', font=self.font, bg=self.PASTEL)
        self.lb8['fg'] = self.ROXO
        self.lb8['font'] = self.font2
        self.lb8.grid(row=7, column=0)
        self.ed8 = Entry(self.frame_direito, fg=self.ROXO, font=self.font)
        self.ed8.grid(row=7, column=1)
        ####################################################################################

        ###################################################################################

        self.lb9 = Label(self.frame_direito, text='Setembro: ', font=self.font, bg=self.PASTEL)
        self.lb9['fg'] = self.ROXO
        self.lb9['font'] = self.font2
        self.lb9.grid(row=8, column=0)
        self.ed9 = Entry(self.frame_direito, fg=self.ROXO, font=self.font)
        self.ed9.grid(row=8, column=1)
        ####################################################################################

        ###################################################################################

        self.lb10 = Label(self.frame_direito, text='Outubro: ', font=self.font, bg=self.PASTEL)
        self.lb10['fg'] = self.ROXO
        self.lb10['font'] = self.font2
        self.lb10.grid(row=9, column=0)
        self.ed10 = Entry(self.frame_direito, fg=self.ROXO, font=self.font)
        self.ed10.grid(row=9, column=1)
        ####################################################################################

        ###################################################################################

        self.lb11 = Label(self.frame_direito, text='Novembro: ', font=self.font, bg=self.PASTEL)
        self.lb11['fg'] = self.ROXO
        self.lb11['font'] = self.font2
        self.lb11.grid(row=10, column=0)
        self.ed11 = Entry(self.frame_direito, fg=self.ROXO, font=self.font)
        self.ed11.grid(row=10, column=1)
        ####################################################################################

        ###################################################################################

        self.lb12 = Label(self.frame_direito, text='Dezembro: ', font=self.font, bg=self.PASTEL)
        self.lb12['fg'] = self.ROXO
        self.lb12['font'] = self.font2
        self.lb12.grid(row=11, column=0)
        self.ed12 = Entry(self.frame_direito, fg=self.ROXO, font=self.font)
        self.ed12.grid(row=11, column=1)
        ####################################################################################

        #BOTÃO PARAR GERAR O GRÁFICO------------------------------------------------------------------------------
        self.botao_do_grafico = Button(self.frame_direito, text='GERAR GRÁFICO', font=self.font2, cursor='hand2')
        self.botao_do_grafico['padx'] = 20
        self.botao_do_grafico['bg'] = self.ROXO
        self.botao_do_grafico['bd'] = 2
        self.botao_do_grafico['fg'] = self.PASTEL
        self.botao_do_grafico['command'] = self.lerMeses
        self.botao_do_grafico.grid(row=12, column=1)

        #BOTÃO PARAR GERAR A PORCENTAGEM------------------------------------------------------------------------------
        self.porcentagem = Button(self.frame_direito, text='GERAR PORCENTAGEM', font=self.font2, cursor='hand2')
        self.porcentagem['padx'] = 20
        self.porcentagem['bg'] = self.ROXO
        self.porcentagem['bd'] = 2
        self.porcentagem['fg'] = self.PASTEL
        self.porcentagem['command'] = self.gerarPorcentagem
        self.porcentagem.grid(row=13, column=1)

    def lerMeses(self):
        #if len(self.ed1.get()) >= 12:
        self.janeiro = float(self.ed1.get())
        self.fevereiro = float(self.ed2.get())
        self.março = float(self.ed3.get())
        self.abril = float(self.ed4.get())
        self.maio = float(self.ed5.get())
        self.junho = float(self.ed6.get())
        self.julho = float(self.ed7.get())
        self.agosto = float(self.ed8.get())
        self.setembro = float(self.ed9.get())
        self.outubro = float(self.ed10.get())
        self.novembro = float(self.ed11.get())
        self.dezembro = float(self.ed12.get())


        self.names = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
                 "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        self.values = [self.janeiro,
                       self.fevereiro,
                       self.março,
                       self.abril,
                       self.maio,
                       self.junho,
                       self.julho,
                       self.agosto,
                       self.setembro,
                       self.outubro,
                       self.novembro,
                       self.dezembro]


        subplots_adjust(bottom=.16, right=0.97)

        tick_params(axis='x', color=self.PASTEL)
        tick_params(axis='y', color=self.AZUL_CINZA)
        xlabel('Meses', color=self.VERMELHO)
        ylabel('Faturamento', color=self.VERMELHO)
        title('Faturamento anual da empresa', color=self.ROXO)

        self.pos = arange(len(self.names)) + .5

        bar(self.pos, self.values, align='center', color=self.ROXO)
        xticks(self.pos, self.names, rotation=30, size='small')
        grid(True)

        show()

    def gerarPorcentagem(self):
        self.Frame_esquerdo.pack_forget()
        self.frame_direito.pack_forget()
        #Frame container-----------------------------------------------
        self.frame = Frame(self.janela, bg=self.PASTEL)
        self.frame.pack()
        #calculos------------------------------------------------------
        self.janeiro = float(self.ed1.get())
        self.fevereiro = float(self.ed2.get())
        self.março = float(self.ed3.get())
        self.abril = float(self.ed4.get())
        self.maio = float(self.ed5.get())
        self.junho = float(self.ed6.get())
        self.julho = float(self.ed7.get())
        self.agosto = float(self.ed8.get())
        self.setembro = float(self.ed9.get())
        self.outubro = float(self.ed10.get())
        self.novembro = float(self.ed11.get())
        self.dezembro = float(self.ed12.get())

        self.total = self.janeiro + \
                     self.fevereiro + self.março + \
                     self.abril + self.maio + self.junho + \
                     self.julho + self.agosto + self.setembro + \
                     self.outubro + self.novembro + self.dezembro

        self.janeiro_porcentagem = self.janeiro * 100 / self.total
        self.fevereiro_porcentagem = self.fevereiro * 100 / self.total
        self.março_porcentagem = self.março * 100 / self.total
        self.abril_porcentagem = self.abril * 100 / self.total
        self.maio_porcentagem = self.maio * 100 / self.total
        self.junho_porcentagem = self.junho * 100 / self.total
        self.julho_porcentagem = self.julho * 100 / self.total
        self.agosto_porcentagem = self.agosto * 100 / self.total
        self.setembro_porcentagem = self.setembro * 100 / self.total
        self.outubro_porcentagem = self.outubro * 100 / self.total
        self.novembro_porcentagem = self.novembro * 100 / self.total
        self.dezembro_porcentagem = self.dezembro * 100 / self.total
        #labels#########################################################################################################
        self.label_porcentagem1 = Label(self.frame, text=f"Janeiro: {self.janeiro_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem1.grid(row=0, column=0)
        #-----------------------------------------------------------------------------------------------------------

        self.label_porcentagem2 = Label(self.frame, text=f"Fevereiro: {self.fevereiro_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem2.grid(row=1, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem3 = Label(self.frame, text=f"Março: {self.março_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem3.grid(row=2, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem4 = Label(self.frame, text=f"Abril: {self.abril_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem4.grid(row=3, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem5 = Label(self.frame, text=f"Maio: {self.maio_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem5.grid(row=4, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem6 = Label(self.frame, text=f"Junho: {self.junho_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem6.grid(row=5, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem7 = Label(self.frame, text=f"Julho: {self.julho_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem7.grid(row=6, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem8 = Label(self.frame, text=f"Agosto: {self.agosto_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem8.grid(row=7, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem9 = Label(self.frame, text=f"Setembro: {self.setembro_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem9.grid(row=8, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem10 = Label(self.frame, text=f"Outubro: {self.outubro_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem10.grid(row=9, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem11 = Label(self.frame, text=f"Novembro: {self.novembro_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem11.grid(row=10, column=0)
        # -----------------------------------------------------------------------------------------------------------
        self.label_porcentagem12 = Label(self.frame, text=f"Dezembro: {self.dezembro_porcentagem:.2f}%", fg=self.ROXO,
                                        bg=self.PASTEL, font=self.font2, pady=5)
        self.label_porcentagem12.grid(row=11, column=0)
        # -----------------------------------------------------------------------------------------------------------
