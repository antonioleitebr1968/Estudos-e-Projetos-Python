palavras = []
with open("hino.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.replace(",", "").replace("!", "").replace(".", "")
        palavras += linha.upper().split()

#print(palavras)

while True:
    palavra = str(input("\033[7;33mInforme uma palavra para saber se está na memória interna:\033[m ")).upper()

    if palavra == 'SAIR':
        break
    elif palavra in palavras:
        print(f'\033[7;34mA palavra \033[7;35m{palavra} \033[7;34mestá na memória!\033[m')
    else:
        print('\033[7;31mPalavra não encontrada na memória.\033[m')

print('\033[7;30mfim do programa.\033[m')
