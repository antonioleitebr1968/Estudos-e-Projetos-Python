#fazer o exercicio 3 utilizando o len e utilizando listas (exercicio 14 do site)
lista = list()
faixa = '-=' * 30
faixa2 = '-' * 60
titulo = 'INTERROGADOR AUTOMÁTICO'
reposta1 = 'X'
final = 'FINISH'
cont = 0
print(f'\033[1;35m{faixa}')
print(f'{titulo:^60}')
print(f'{faixa}')
while reposta1 not in 'SN':
    reposta1 = str(input('Telefonou para a vítima? [S/N] ')).upper().strip()[0]
    if reposta1 == 'S':
        lista.append(1)
    if reposta1 == 'N':
        cont += 1
reposta2 = 'X'
while reposta2 not in 'SN':
    reposta2 = str(input('Esteve no local do crime? [S/N] ')).upper().strip()[0]
    if reposta2 == 'S':
        lista.append(2)
    if reposta2 == 'N':
        cont += 1
reposta3 = 'X'
while reposta3 not in 'SN':
    reposta3 = str(input('Mora perto da vítima? [S/N] ')).upper().strip()[0]
    if reposta3 == 'S':
        lista.append(3)
    if reposta3 == 'N':
        cont += 1
reposta4 = 'X'
while reposta4 not in 'SN':
    reposta4 = str(input('Devia para a vítima? [S/N] ')).upper().strip()[0]
    if reposta4 == 'S':
        lista.append(4)
    if reposta4 == 'N':
        cont += 1
reposta5 = 'X'
while reposta5 not in 'SN':
    reposta5 = str(input('Já trabalhou com a vítima? [S/N] ')).upper().strip()[0]
    if reposta5 == 'S':
        lista.append(5)
    if reposta5 == 'N':
        cont += 1
print(f'{faixa2}')
if len(lista) == 2:
    print('Você foi conciderado[a] \033[1;32mSuspeito[a] !!!\033[m')
if len(lista) == 3 or len(lista) == 4:
    print('Você foi conciderado[a] \033[1;33mcúmplice !!!\033[m')
if len(lista) == 5:
    print('Você foi conciderado[a] \033[1;31massassino !!!!!\033[m')
if cont == 5:
    print('Você foi conciderado[a] \033[1;36minocente !!!\033[m')
print(f'\033[1;35m{faixa2}')
print(f'{final:^60}\033[m')

