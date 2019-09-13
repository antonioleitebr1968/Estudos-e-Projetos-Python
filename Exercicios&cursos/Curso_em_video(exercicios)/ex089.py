"""Crie um programa que leia nome e duas notas de
vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de
cada um e permita que o úsuario possa mostrar as
notas de cada aluno individualmente."""

from time import sleep
alunos = []
provisorio = []
nome = []
notas = []
while True:
    n = str(input('Nome: ')).strip().capitalize()
    n1 = float(input('Nota 1º: '))
    n2 = float(input('Nota 2º: '))
    média = (n1 + n2) / 2
    nome.append(n)
    notas.append(n1)
    notas.append(n2)
    notas.append(média)
    provisorio.append(nome[:])
    provisorio.append(notas[:])
    alunos.append(provisorio[:])
    nome.clear()
    notas.clear()
    provisorio.clear()
    resp = 'X'
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().capitalize()[0]
    if resp == 'N':
        break
boletim = ' Nº      NOME        MÉDIA'
print('-=' * 30)
print(f'{boletim}')
print('-' * 30)
for i in range(0, len(alunos)):
    nomess = f'{alunos[i][0][0]}'
    notass = f'{alunos[i][1][2]:.1f}'
    print(f' {i}', end='')
    print(f' {nomess.center(18, " ")}', end='')
    print(f' {notass.center(5, " ")}')
while True:
    print('-' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    for i in range(0, len(alunos)):
        nota1 = f'{alunos[i][1][0]:.1f}'
        nota2 = f'{alunos[i][1][1]:.1f}'
        if mostrar == i:
            print(f'Notas de {alunos[i][0][0]} são {nota1} e {nota2}')
    if mostrar == 999:
        break
print()
print('FINALIZANDO...')
sleep(1)
fim = '<<< VOLTE SEMPRE >>>'
print(f'{fim.center(60, "=")}')
