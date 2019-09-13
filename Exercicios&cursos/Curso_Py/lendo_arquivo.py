arq = open("teste_aula.txt", "r")#r para ler

#print(arq.read())

#lendo linha a linha

#print(arq.readline(5))#informando quantidade de caracteres
#print(arq.readline())

linhas = arq.readlines()#retorna uma lista com todas as linha do arquivo
#print(linhas, linhas[2])
arq.close()
