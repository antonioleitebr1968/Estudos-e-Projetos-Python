# Abrindo o arquivo para escrita, mantendo o conteúdo
with open("arquivo_teste_dois.txt", "a") as arquivo:
    arquivo.write("Linha adicionada")

# como o modo "r" (leitura) é o padrão, caso eu
# não informe, será aberto como somente leitura
with open("arquivo_teste_dois.txt") as arquivo:
    for linha in arquivo:
        print(linha)
