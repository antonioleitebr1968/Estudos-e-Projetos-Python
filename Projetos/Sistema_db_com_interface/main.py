from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode
from functools import partial ##necessario para passar parametros a uma função sem invoca-lá


class Main(object):
    def __init__(self):
        #############VARIÁVEIS CONTENDO CORES##################
        self.AZUL = '#48D1CC'
        self.CINZA = '#A9A9A9'
        self.CINZA_CLARO = '#778899'
        self.CINZA_MAIS_CLARO = '#DCDCDC'
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
        self.AZURE = '#F0FFFF'
        self.ROXO_COISADO = '#4B0082'
        self.CINZA2 = '#778899'
        self.OrangeRed = '#FF4500'
        self.Gold = '#FFD700'

        #fontes
        self.font = ('Verdana', 25, 'bold')
        self.font2 = ('papyrus', 17, 'bold')
        self.fontGrande = ('papyrus', 30, 'bold')
        self.font3 = ('Verdana', 15, 'bold')
        self.font4 = ('Bauhaus 93', 25, 'bold')
        self.font5 = ('Verdana', 23, 'bold')

        self.janela = Tk()
        self.janela.title("Banco de Dados")
        #self.janela.wm_iconbitmap('imagens\\g1.ico')
        self.janela.resizable(False, False)
        self.janela.geometry("600x500+50+100")
        self.janela["bg"] = self.AZUL_CINZA
        #self.dadosConexao = ""


        self.configLabels = {'bg': self.AZUL_CINZA, 'fg': 'black', 'font': self.font2, 'pady': 20}
        self.configEntrys = {'fg': 'White', 'font': self.font3, 'justify': CENTER, 'width': 15, 'bg': self.CINZA}


        self.criarTelaLogin()

        self.janela.mainloop()



    def criarTelaLogin(self):
        self.frameLogin = Frame(self.janela, bg=self.AZUL_CINZA)
        self.frameLogin.pack()

        self.labelBanco = Label(self.frameLogin, text="Banco de dados:", **self.configLabels)
        self.labelBanco.grid(row=0, column=0)

        self.entradaBanco = Entry(self.frameLogin, **self.configEntrys)
        self.entradaBanco.grid(row=1, column=0)
        

        self.labelUsuario = Label(self.frameLogin, text="Usuário:", **self.configLabels)
        self.labelUsuario.grid(row=2, column=0)

        self.entradaUsuario = Entry(self.frameLogin, **self.configEntrys)
        self.entradaUsuario.grid(row=3, column=0)

        self.labelSenha = Label(self.frameLogin, text="Senha:", **self.configLabels)
        self.labelSenha.grid(row=4, column=0)

        self.entradaSenha = Entry(self.frameLogin, **self.configEntrys, show='*')
        self.entradaSenha.grid(row=5, column=0)

        #criando botão
        self.botaoEntrar = PhotoImage(file='imgs\\entrar.png')  # caminho da img
        self.but = Button(self.frameLogin, cursor='hand2', pady=10, bd=2, bg=self.AZUL_CINZA,
                          activebackground=self.CINZA_MAIS_CLARO,
                          command=self.validarLogin, text='ENTRAR', padx=30, relief=GROOVE, width=150)

        self.but['image'] = self.botaoEntrar
        self.but.image = self.botaoEntrar
        self.but.grid(row=6, column=0)

        self.labelInfo = Label(self.frameLogin, text="", bg=self.AZUL_CINZA, fg="red",
                          font=self.font2, pady=10)
        self.labelInfo.grid(row=7, column=0)


    def destruirLogin(self):
        self.frameLogin.destroy()
        self.criarMenuAgenda()



    def validarLogin(self):
        self.dadosConexao = {'user': str(self.entradaUsuario.get()),
                             'password': str(self.entradaSenha.get()),
                             'host': '127.0.0.1',
                             'database': str(self.entradaBanco.get())}

        try:
            if self.dadosConexao['database'] == 'sistemadb' and self.dadosConexao['password'] == 'senhaAqui' and self.dadosConexao['user'] == 'root':
                messagebox.showinfo('Desculpe!', 'Sem suporte para esse Banco!')
            else:
                self.conexao = mysql.connector.connect(**self.dadosConexao)
                self.destruirLogin()
        except mysql.connector.Error as erro:
            #erro de acesso negado
            if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.labelInfo["text"] = "Usuario ou senha incorreto."
                #erro de banco não existente
            elif erro.errno == errorcode.ER_BAD_DB_ERROR:
                self.labelInfo["text"] = "Banco de dados não existe."
            else:
                print(erro)


    def destruirMenuAgenda(self):
        self.framePai.destroy()
        self.constroiTelaCadastro()


    def criarMenuAgenda(self):

        if self.dadosConexao['database'] == 'agenda':
            #mudanças --------------------------------
            self.font4 = ('Bauhaus 93', 25, 'bold')
            self.janela.title("Agenda")
            self.janela.geometry("800x600+50+100")
            self.janela["bg"] = self.CINZA

            self.congiButtons = {"bg": self.AZUL_CINZA, "fg": "black",
                                 "font": self.font2, "cursor": "hand2",
                                 "bd": 2, "relief": GROOVE, 'width': 30}

            self.congiLabel2 = {"bg": self.CINZA, "fg": 'black',
                                "font": self.font4, "pady": 10}
            #-----------------------------------------
            self.framePai = Frame(self.janela, bg=self.CINZA)
            self.framePai.pack()

            self.lb1 = Label(self.framePai, text="BEM VINDO AO SISTEMA DE CADASTRO", **self.congiLabel2)
            self.lb1.grid(row=0, column=0)

            self.lb2 = Label(self.framePai, text="ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS", **self.congiLabel2)
            self.lb2.grid(row=1, column=0)

            self.btn1 = Button(self.framePai, text="CADASTAR UM CONTATO", **self.congiButtons,
                               command=self.destruirMenuAgenda)
            self.btn1.grid(row=2, column=0)

            self.btn2 = Button(self.framePai, text="ALTERAR UM CONTATO", **self.congiButtons)
            self.btn2.grid(row=3, column=0)

            self.btn3 = Button(self.framePai, text="LISTAR CONTATOS", **self.congiButtons)
            self.btn3.grid(row=4, column=0)

            self.btn4 = Button(self.framePai, text="EXPORTAR CONTATOS", **self.congiButtons)
            self.btn4.grid(row=5, column=0)

            self.btn5 = Button(self.framePai, text="EXCLUIR CONTATO", **self.congiButtons)
            self.btn5.grid(row=6, column=0)

            self.chamarEventosBtns()


    def constroiTelaCadastro(self):
        self.janela.geometry("1000x700+50+100")
        self.janela["bg"] = self.CINZA
        self.congiButtons2 = {"bg": self.AZUL_CLARO_DA_PESTE, "fg": "black",
                             "font": self.font4, "cursor": "hand2",
                             "bd": 2, "relief": GROOVE, 'width': 12,
                             'height': 1}

        self.congiLabel2 = {"bg": self.CINZA, "fg": 'black',
                            "font": self.font4, "pady": 10}

        self.congiLabel3 = {"bg": self.AZUL_CLARO_DA_PESTE, "fg": 'black',
                            "font": self.font2, 'bd': 0, "justify": RIGHT, 'pady': 30}

        self.congiLabel4 = {"bg": self.CINZA, "fg": 'black',
                            "font": self.font2, 'bd': 0}

        self.frameTitulo = Frame(self.janela, bg=self.CINZA)
        self.frameTitulo.pack()
        self.frameCentral = Frame(self.janela, bg=self.AZUL_CLARO_DA_PESTE, bd=10, relief=SUNKEN, pady=50)
        self.frameCentral.pack()

        self.lb1 = Label(self.frameTitulo, text="CADASTRANDO UM NOVO CONTATO", **self.congiLabel2)
        self.lb1.grid(row=0, column=0)

        self.labelNome = Label(self.frameCentral, text='Informe o nome do contato (obrigatório)=>', **self.congiLabel3
                               , width=30)
        self.labelNome.grid(row=1, column=0, sticky=W)

        self.entryNome = Entry(self.frameCentral, **self.congiLabel4)
        self.entryNome.grid(row=1, column=1)

        self.labelTelefone = Label(self.frameCentral, text='Informe o telefone do contato (obrigatório)=>',
                                   **self.congiLabel3
                                   , width=30)
        self.labelTelefone.grid(row=2, column=0, sticky=W)

        self.entryTelefone = Entry(self.frameCentral, **self.congiLabel4)
        self.entryTelefone.grid(row=2, column=1)

        self.labelCelular = Label(self.frameCentral, text='Informe o celular do contato (obrigatório)=>',
                                  **self.congiLabel3
                                  , width=30)
        self.labelCelular.grid(row=3, column=0, sticky=W)

        self.entryCelular = Entry(self.frameCentral, **self.congiLabel4)
        self.entryCelular.grid(row=3, column=1, sticky=W)

        self.btCadastro = Button(self.frameCentral, text="CADASTRAR", **self.congiButtons2, command=self.cadastrar)
        self.btCadastro.grid(row=4, column=0, columnspan=2)

        self.labelInformativo = Label(self.frameCentral, text='',
                                      **self.congiLabel3)
        self.labelInformativo.grid(row=5, column=0, columnspan=2)

        self.btVoltar = Button(self.frameCentral, text="Voltar", width=5, font=self.font2, bg=self.CINZA, fg='white'
                               , command=self.destroiTelaCadastro, cursor='hand2')
        self.btVoltar.grid(row=6, column=0, sticky=SW)

        self.btCadastro.bind('<Enter>', partial(self.configBt3, self.btCadastro, self.CINZA, 20))
        self.btCadastro.bind('<Leave>', partial(self.configBt3, self.btCadastro, self.AZUL_CLARO_DA_PESTE, 12))

    def destroiTelaCadastro(self):
        self.frameTitulo.destroy()
        self.frameCentral.destroy()
        self.criarMenuAgenda()

    def cadastrar(self):

        self.nome = str(self.entryNome.get())
        self.telefone = str(self.entryTelefone.get())
        self.celular = str(self.entryCelular.get())

        if self.nome and self.telefone and self.celular:
            try:
                self.contato = []
                self.contato.append(self.nome)
                self.contato.append(self.telefone)
                self.contato.append(self.celular)

                self.cursor = self.conexao.cursor()
                self.comando_sql = "insert into contatos (nome, telefone, celular) values(%s, %s, %s)"
                self.cursor.execute(self.comando_sql, self.contato)
                self.conexao.commit()  # gravar
                self.labelInformativo['fg'] = self.OrangeRed
                self.labelInformativo['font'] = self.font
                self.labelInformativo['text'] = f'Contato {self.nome} cadastrado com sucesso!'
                #self.fecharConexao()
            except Exception as erro:
                self.labelInformativo['fg'] = 'red'
                self.labelInformativo['font'] = self.font
                self.labelInformativo['text'] = "Ocorreu um erro!"
                print(erro)
        else:
            self.labelInformativo['font'] = self.font
            self.labelInformativo['fg'] = self.OrangeRed
            self.labelInformativo['text'] = 'Todos os campos são obrigatórios!'

    def chamarEventosBtns(self):
        self.btn1.bind('<Enter>', partial(self.configurarBt2, self.btn1, self.VERMELHO, 10, 32, self.font5))
        self.btn1.bind('<Leave>', partial(self.configurarBt2, self.btn1, self.AZUL_CINZA, 2, 30, self.font2))

        self.btn2.bind('<Enter>', partial(self.configurarBt2, self.btn2, self.VERMELHO, 10, 32, self.font5))
        self.btn2.bind('<Leave>', partial(self.configurarBt2, self.btn2, self.AZUL_CINZA, 2, 30, self.font2))

        self.btn3.bind('<Enter>', partial(self.configurarBt2, self.btn3, self.VERMELHO, 10, 32, self.font5))
        self.btn3.bind('<Leave>', partial(self.configurarBt2, self.btn3, self.AZUL_CINZA, 2, 30, self.font2))

        self.btn4.bind('<Enter>', partial(self.configurarBt2, self.btn4, self.VERMELHO, 10, 32, self.font5))
        self.btn4.bind('<Leave>', partial(self.configurarBt2, self.btn4, self.AZUL_CINZA, 2, 30, self.font2))

        self.btn5.bind('<Enter>', partial(self.configurarBt2, self.btn5, self.VERMELHO, 10, 32, self.font5))
        self.btn5.bind('<Leave>', partial(self.configurarBt2, self.btn5, self.AZUL_CINZA, 2, 30, self.font2))

    def configurarBt2(self, obj, bg, bd, width, font, event):
        obj.configure(bg=bg, bd=bd, width=width, font=font)

    def configBt3(self, obj, bg, width, event):
        obj.configure(bg=bg, width=width)

    def fecharConexao(self):
        self.cursor.close()
        self.conexao.close()

if __name__ == '__main__':
    Main()
