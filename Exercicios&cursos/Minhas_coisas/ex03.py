faixa = '-' * 60
faixa2 = '-=' * 30
titulo = 'Interrogador'
cont = 0
a = 'X'
print(faixa2)
print(f'{titulo:^60}')
print(faixa2)
while a not in 'SN':
    a = str(input('Telefonou para a vítima? [S/N] ')).upper().strip()[0]
if a == 'S':
    cont += 1
b = 'X'
while b not in 'SN':
    b = str(input('Esteve no local do crime? [S/N] ')).upper().strip()[0]
if b == 'S':
    cont += 1
c = 'X'
while c not in 'SN':
    c = str(input('Mora perto da vítima? [S/N] ')).upper().strip()[0]
if c == 'S':
    cont += 1
d = 'X'
while d not in 'SN':
    d = str(input('Devia para a vítima? [S/N] ')).upper().strip()[0]
if d == 'S':
    cont += 1
e = 'X'
while e not in 'SN':
    e = str(input('Já trabalhou com a vítima? [S/N] ')).upper().strip()[0]
if e == 'S':
    cont += 1
if cont == 2:
    print('Você foi conciderado[a] suspeito[a] !!')
if cont >= 3:
    print('Você foi conciderado[a] cúmplice !!')
if cont == 5:
    print('Você foi conciderado[a] assassino[a] !!')
print(faixa)




