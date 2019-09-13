import os.path
import time

while True:
    nome = input("Informe um nome de arquivo (informe 'sair' para finalizar): ")
    if nome.upper() == "SAIR":
        break
    if os.path.exists(nome):
        print("Nome:", nome)
        print("Tamanho:", os.path.getsize(nome), "bytes")
        print("Data da criação:", time.ctime(os.path.getctime(nome)))
        print("Data de modificação:", time.ctime(os.path.getmtime(nome)))
        print("Data de acesso:", time.ctime(os.path.getatime(nome)))
    else:
        print(nome, "NÃO existe!!!")