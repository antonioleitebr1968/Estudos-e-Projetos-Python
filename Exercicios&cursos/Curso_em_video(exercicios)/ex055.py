#minha maneira
'''peso1 = float(input('Primeiro peso: '))
peso2 = float(input('Segundo peso: '))
peso3 = float(input('Terceiro peso: '))
peso4 = float(input('Quarto peso: '))
peso5 = float(input('Quinto peso: '))
print('O maior peso é {}kg'.format(max(peso1, peso2, peso3, peso4, peso5)))
print('O menor peso é {}kg'.format(min(peso1, peso2, peso3, peso4, peso5)))'''
#proff
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))



