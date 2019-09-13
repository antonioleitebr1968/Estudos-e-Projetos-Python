lista = list()
while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('O valor já existe na lista, por tanto ele não será adicionado!')

    resposta = 'X'
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-=' * 25)
lista.sort()
print('Os valores digitados foram: ', end=' ')
for v in lista:
    print(f'{v}', end=' ')
