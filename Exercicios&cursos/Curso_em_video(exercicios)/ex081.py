lista = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resposta = 'X'
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decresente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
