import os
import platform
import mysql.connector

dados_conexao = {'user':'root',
                 'password':'senhaAqui',
                 'host':'127.0.0.1',
                 'database':'agenda'}

def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def sair():
    print('Obrigado por utilizar o sistema!')
    os._exit(0)#0 para informar que está saindo sem erros
    
def mensagem_menu_principal():
    limpar_tela()
    print('**************************************************')
    print('*       BEM VINDO AO SISTEMA DE CADASTRO         *')
    print('*------------------------------------------------*')
    print('*       ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS       *')
    print('*             1 - CADASTAR UM CONTATO            *')
    print('*             2 - ALTERAR UM CONTATO             *')
    print('*             3 - LISTAR CONTATOS                *')
    print('*             4 - EXPORTAR CONTATOS              *')
    print('*             5 - EXCLUIR CONTATO                *')
    print('*             0 - SAIR DO SISTEMA                *')
    print('**************************************************')
    

def mensagem_menu_alterar():
    limpar_tela()
    print('**************************************************')
    print('*         ALTERAR UM CONTATO EXISTENTE           *')
    print('*------------------------------------------------*')
    print('* ESCOLHA UMA DAS OPÇÕES PARA LOCALIZAR O CONTATO*')
    print('*             1 - ID                             *')
    print('*             2 - NOME                           *')
    print('*             3 - TELEFONE                       *')
    print('*             4 - CELULAR                        *')
    print('*             0 - MENU PRINCIPAL                 *')
    print('**************************************************')


def mensagem_menu_excluir():
    limpar_tela()
    print('**************************************************')
    print('*         EXCLUIR UM CONTATO EXISTENTE           *')
    print('*------------------------------------------------*')
    print('* ESCOLHA UMA DAS OPÇÕES PARA LOCALIZAR O CONTATO*')
    print('*             1 - ID                             *')
    print('*             2 - NOME                           *')
    print('*             3 - TELEFONE                       *')
    print('*             4 - CELULAR                        *')
    print('*             0 - MENU PRINCIPAL                 *')
    print('**************************************************')

def mensagem_cadastrar():
    limpar_tela()
    print('**************************************************')
    print('*          CADASTRANDO UM NOVO CONTATO           *')
    print('**************************************************')



def cadastrar():
    mensagem_cadastrar()
    nome = input("Informe o nome do contato (obrigatório): ")
    telefone = input("Informe o telefone do contato (obrigatório): ")
    celular = input("Informe o celular do contato (obrigatório): ")

    if nome and telefone and celular:
        confirmar = input(f"Confirmar cadastro do contato: {nome}? (S/N): ")[0].upper()
        if confirmar == 'S':
            try:
                contato = []
                contato.append(nome)
                contato.append(telefone)
                contato.append(celular)
                conexao = mysql.connector.connect(**dados_conexao)
                cursor = conexao.cursor()
                comando_sql = "insert into contatos (nome, telefone, celular) values(%s, %s, %s)"
                cursor.execute(comando_sql, contato)
                conexao.commit()#gravar
                cursor.close()
                conexao.close()
                input("Cadastrado com sucesso!\nPrecione uma tecla para voltar ao menu principal...")
            except Exception as erro:
                input(f"Ocorreu um erro no cadastro: {erro}.\nPrecione uma tecla para voltar ao menu principal...")
        else:
            input("Cadastro cancelado.\nPrecione uma tecla para voltar ao menu principal...")
    else:
        input("Todos os campos são obrigatórios.\nPrecione uma tecla para voltar ao menu principal...")

    menu_principal()



def excluir(contato):
    try:
        comando_sql = f"delete from contatos where id = {contato['id']}"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        print('==================================================')
        print(f"ID: {contato['id']}")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Celular: {contato['celular']}")
        print('==================================================')

        confirmar = input("Tem certeza que deseja excluir o contato? ").upper()
        if confirmar == "S":
            conexao.commit()
            cursor.close()
            conexao.close()
            input("Contato deletado com sucesso.\nPressione uma tecla para voltar ao menu principal...")
        else:
            cursor.close()
            conexao.close()
            input("Exclusão cancelada.\nPressione uma tecla para voltar ao menu principal...")
    except:
        input("Falha ao deletar.\nPressione uma tecla para voltar ao menu principal...")
    menu_principal()
    


def alterar():
    mensagem_menu_alterar()
    opcao = input("Informe a opção desejada: ")
    try:
        acoes_menu_alterar[opcao]()
    except:
        input("Opção inválida\nPrecione uma tecla para voltar...")
        alterar()




def pesquisa_por_id_para_exclusao(id=""):
    try:
        if not id:
            id = input("Informe o id do contato: ")
        comando_sql = f'select id, nome, telefone, celular from contatos where id = {id}'
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = ""
        for id, nome, telefone, celular in cursor:
            contato = {"id":id,"nome":nome,
                       "telefone":telefone,
                       "celular":celular}
        cursor.close()
        conexao.close()
        excluir(contato)
        
    except Exception as erro:
        print("Ocorreu erro na busca por id! ", erro)
        input("Precione uma tecla para voltar...")
        menu_principal()


def pesquisar_id(id=""):
    try:
        if not id:
            id = input("Informe o id do contato: ")
        comando_sql = f'select id, nome, telefone, celular from contatos where id = {id}'
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = ""
        for id, nome, telefone, celular in cursor:
            contato = {"id":id,"nome":nome,
                       "telefone":telefone,
                       "celular":celular}
        cursor.close()
        conexao.close()
        alterar_contato(contato)
        
    except Exception as erro:
        print("Ocorreu erro na busca por id! ", erro)
        input("Precione uma tecla para voltar...")
        alterar()


def pesquisar_nome():
    try:
        nome = input("Informe o nome do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where nome like '%{nome}%' limit 1"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id":id,"nome":nome,
                       "telefone":telefone,
                       "celular":celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: \nid: {contato['id']}\nNome: {contato['nome']}\ntelefone: {contato['telefone']}\ncelular: {contato['celular']}")
            
        pesquisar_id(contato['id'])
        
    except Exception as erro:
        print("Ocorreu erro na busca por nome! ", erro)
        input("Precione uma tecla para voltar...")
        alterar()



def pesquisar_telefone():
    try:
        telefone = input("Informe o telefone do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where telefone = '{telefone}'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id":id,
                       "nome":nome,
                       "telefone":telefone,
                       "celular":celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: \nid: {contato['id']}\nNome: {contato['nome']}\ntelefone: {contato['telefone']}\ncelular: {contato['celular']}")
            
        pesquisar_id(contato['id'])
        
    except Exception as erro:
        print("Ocorreu erro na busca por telefone! ", erro)
        input("Precione uma tecla para voltar...")
        alterar()



def pesquisar_celular():
    try:
        celular = input("Informe o celular do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where celular = '{celular}'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id":id,"nome":nome,
                       "telefone":telefone,
                       "celular":celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: \nid: {contato['id']}\nNome: {contato['nome']}\ntelefone: {contato['telefone']}\ncelular: {contato['celular']}")
            
        pesquisar_id(contato['id'])
        
    except Exception as erro:
        print("Ocorreu erro na busca por celular! ", erro)
        input("Precione uma tecla para voltar...")
        alterar()



def listar():
    try:
        comando_sql = "select id, nome, telefone, celular from contatos order by id asc"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        print('==================================================')
        for id, nome, telefone, celular in cursor:
            print(f"ID: {id}")
            print(f"Nome: {nome}")
            print(f"Telefone: {telefone}")
            print(f"Celular: {celular}")
            print('==================================================')
        cursor.close()
        conexao.close()
        input("Pressione uma tecla para voltar ao menu principal...")
        
    except:
        print("Ocorreu erro ao listar.", erro)
    menu_principal()




def exportar():
    try:
        nome_arquivo = input("Informe o nome do arquivo: ")
        
        comando_sql = "select id, nome, telefone, celular from contatos order by id asc"
        contatos = []
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        
        cursor.execute(comando_sql)
        for id, nome, telefone, celular in cursor:
           contatos.append({"id": id, "nome": nome, "telefone": telefone, "celular": celular})
           
        cursor.close()
        conexao.close()
        
        arquivo = open(nome_arquivo, "w", encoding="utf-8")

        for contato in contatos:
            registro = []
            registro.append(f"{contato['id']};{contato['nome']};{contato['telefone']};{contato['celular']}\n")
            arquivo.writelines(registro)
            #print(registro)

        arquivo.close()
        print("Exportação realizada.")
        input("Pressione uma tecla para voltar ao menu principal...")
        menu_principal()
    except Exception as err:
        print("Ocorreu erro na função exportar! ", err)
        input("Pressione uma tecla para voltar ao menu principal...")
        menu_principal()

    
def alterar_contato(contato):
    nome = input(f"Informe o nome do contato ({contato['nome']}): ") or contato['nome']
    telefone = input(f"Informe o telefone do contato ({contato['telefone']}): ") or contato['telefone']
    celular = input(f"Informe o celular do contato ({contato['celular']}): ") or contato['celular']
    
    confirma = input(f"Confirmar alteração do contato: {nome}? (S/N): ")
    if confirma.upper() == 'S':
        try:
            comando_sql = f"update contatos set nome = '{nome}', telefone = '{telefone}', celular = '{celular}' where id = {contato['id']}"
            conexao = mysql.connector.connect(**dados_conexao)
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            conexao.commit()
            cursor.close()
            conexao.close()  
            input("Contato alterado com sucesso.\nPrecione uma tecla para voltar... ")
        except:
            input("Ocorreu um erro na alteração.\nPrecione uma tecla para voltar... ")
    else:
        input("Alteração cancelada.\nPrecione uma tecla para voltar... ")
    alterar()
    

    
def menu_principal():
    try:
        mensagem_menu_principal()
        opcao = input("Informe a opção desejada: ")
        acoes_menu_principal[opcao]()
    except:
        input("Opção inválida.\nPrecione uma tecla para voltar ao menu principal.")
        menu_principal()


acoes_menu_principal = {
    '1':cadastrar,
    '2':alterar,
    '3':listar,
    '4':exportar,
    '5':pesquisa_por_id_para_exclusao,
    '0':sair,
    }

acoes_menu_alterar = {
    '1': pesquisar_id,
    '2': pesquisar_nome,
    '3': pesquisar_telefone,
    '4': pesquisar_celular,
    '0': menu_principal
    }


if __name__ == "__main__":
    menu_principal()







    
