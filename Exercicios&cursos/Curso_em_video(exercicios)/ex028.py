#from random import choice
#print('-=-' * 100)
#print(' ' * 50, 'Vou pensar em um número tente adivinhar...')
#print('-=-' * 100)
#num = int(input('Em que número eu pensei? '))
#lista = [0, 1, 2, 3, 4, 5]
#escolhido = choice(lista)
#print(escolhido)
#if num == escolhido:
#    print('Acertou mizeravi!')
#else:
#    print('Hahaha eu ganhei!')
#print(' ')
#print('-' * 65, 'ATÉ MAIS!', '-' * 80)
from random import randint
from time import  sleep
computador = randint(0, 5)
print('\033[1;31m-=-\033[m' * 20)
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;31m-=-\033[m' * 20)
jogador = int(input('\033[1;31mem que número eu pensei?\033[m '))
print('\033[1;33mPROCESSANDO...\033[m')
sleep(2)
if jogador == computador:
    print('\033[1;35mACERTO MIZERAVI!\033[m')
else:
    print('\033[1;31mPENSEI EM {} E NÃO NO {}, IHUUUU GANHEI!\033[m'.format(computador,jogador))
print('\033[1;31m-=-\033[m' *8, '\033[1;34mAté a proxima!\033[m','\033[1;31m-=-\033[m' * 7 )
