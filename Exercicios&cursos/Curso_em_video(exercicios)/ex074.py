from random import randint
Um = randint(0, 10)
Dois = randint(0, 10)
Três = randint(0, 10)
Quatro = randint(0, 10)
Cinco = randint(0, 10)

tupla = (Um, Dois, Três, Quatro, Cinco)
print('Os valores sorteados foram: ', end=' ')
for números in tupla:
    print(números, end=' ')
print(f'\nO maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')
print('-=' * 20)
#proff --------------------------------------------------
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),# isso é uma variável composta. Uma variável composta é colocada dentro de parenteses podendo assim guardar mais intens dentro da mesma
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
