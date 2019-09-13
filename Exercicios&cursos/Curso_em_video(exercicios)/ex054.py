#minha solução
'''from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    anonasc = ano - nasc
    if anonasc < 21:
        menor = menor + 1
    elif anonasc >= 21:
        maior = maior + 1
print('{} pessoas são menor de idade'.format(menor), end=' ')
print('e {} pessoas são maior de idade.'.format(maior))'''
#solução do Guanabara
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))



