lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resposta = 'X'
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('A lista completa é ', end='')
for i in lista:
    print(i, end=' | ')
print('\nA lista de pares é ', end='')
for i in lista:
    if i % 2 == 0:
        print(i, end=' | ')
print('\nA lista de ímpares é ', end='')
for i in lista:
    if i % 2 == 1:
        print(i, end=' | ')

#proff ------------------------------------------------------------------------
'''num = list()
pares = list()
ímapares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):#O (I) é o indece e o (V) é o valor
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímapares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímapares}')'''
