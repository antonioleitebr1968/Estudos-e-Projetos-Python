'''Aprimore o desafio anterior, mostre no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

"""conte = contest = contd = totpares = totterceiracoluna = 0
linhazero = []
linhaum = []
linhadois = []
colunaprincipal = []
pares = []
terceiracoluna = []
for c in range(0, 3):
    num = int(input(f'Digite um valor para [{conte}, {contd}]: '))
    contest += 1
    if num % 2 == 0:
        pares.append(num)
    if contest >= 1:
        contd += 1
    linhazero.append(num)
conte = 1
contd = contest = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [{conte}, {contd}]: '))
    contest += 1
    if num % 2 == 0:
        pares.append(num)
    if contest >= 1:
        contd += 1
    linhaum.append(num)
conte = 2
contd = contest = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [{conte}, {contd}]: '))
    contest += 1
    if num % 2 == 0:
        pares.append(num)
    if contest >= 1:
        contd += 1
    linhadois.append(num)
colunaprincipal.append(linhazero)
colunaprincipal.append(linhaum)
colunaprincipal.append(linhadois)
print('-=' * 25)
print(f'[ {colunaprincipal[0][0]} ]', end='')
print(f'[ {colunaprincipal[0][1]} ]', end='')
print(f'[ {colunaprincipal[0][2]} ]')
print(f'[ {colunaprincipal[1][0]} ]', end='')
print(f'[ {colunaprincipal[1][1]} ]', end='')
print(f'[ {colunaprincipal[1][2]} ]')
print(f'[ {colunaprincipal[2][0]} ]', end='')
print(f'[ {colunaprincipal[2][1]} ]', end='')
print(f'[ {colunaprincipal[2][2]} ]')
print('-=' * 25)
for n in pares:
    totpares += n
print(f'A soma de todos os valores pares digitados é: {totpares}')
terceiracoluna.append(colunaprincipal[0][2])
terceiracoluna.append(colunaprincipal[1][2])
terceiracoluna.append(colunaprincipal[2][2])
for i in terceiracoluna:
    totterceiracoluna += i
print(f'A soma dos valores da terceira coluna é: {totterceiracoluna}')
print(f'O maior valor da segunda linha é: {max(linhaum)}')"""

# ==============================================================================
somaP = maior = somacol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaP += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'Soma de todos os valores pares digitados: {somaP}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'Soma de todos os valores da terceira coluna: {somacol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma de todos os valores da segunda linha é: {maior}')
