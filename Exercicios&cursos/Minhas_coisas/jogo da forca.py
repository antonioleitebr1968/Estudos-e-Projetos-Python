# rascunho
palavra_secreta = ["M", "A", "C", "E", "I", "O"]
letras_descobertas = []

print('jogo da forca')

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append("-")

acertou = False

while acertou == False:
    letra = str(input('\nDigite a aletra: ')).upper().strip()

    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra

        print(letras_descobertas[i], end='')

    acertou = True

    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == "-":
            acertou = False

print("\nParabéns")
