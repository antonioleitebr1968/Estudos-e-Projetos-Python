'''Crie um programa que crie uma matriz de
dimensão 3x3 e preencha com valores lidos
pelo teclado. No final, mostre a matriz
na tela, com a formatação correta.'''

"""conte = contest = contd = 0
linhazero = []
linhaum = []
linhadois = []
colunaprincipal = []
for c in range(0, 3):
    num = int(input(f'Digite um valor para [{conte}, {contd}]: '))
    contest += 1
    if contest >= 1:
        contd += 1
    linhazero.append(num)
conte = 1
contd = contest = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [{conte}, {contd}]: '))
    contest += 1
    if contest >= 1:
        contd += 1
    linhaum.append(num)
conte = 2
contd = contest = 0
for c in range(0, 3):
    num = int(input(f'Digite um valor para [{conte}, {contd}]: '))
    contest += 1
    if contest >= 1:
        contd += 1
    linhadois.append(num)
colunaprincipal.append(linhazero)
colunaprincipal.append(linhaum)
colunaprincipal.append(linhadois)
print('-=' * 20)
print(f'[ {colunaprincipal[0][0]} ]', end='')
print(f'[ {colunaprincipal[0][1]} ]', end='')
print(f'[ {colunaprincipal[0][2]} ]')
print(f'[ {colunaprincipal[1][0]} ]', end='')
print(f'[ {colunaprincipal[1][1]} ]', end='')
print(f'[ {colunaprincipal[1][2]} ]')
print(f'[ {colunaprincipal[2][0]} ]', end='')
print(f'[ {colunaprincipal[2][1]} ]', end='')
print(f'[ {colunaprincipal[2][2]} ]')"""


# proff ------------------------------------------------------------------------------


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
