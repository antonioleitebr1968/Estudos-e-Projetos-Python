from time import sleep
from random import randint
computador = randint(0, 10)
cont = 0
print('\033[1;31m=' * 70)
print('Olá, eu sou o seu computador inteligente...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
print('\033[1;31m=\033[m' * 70)
n = int(input('\033[1;36mQual é o seu palpite? '))
cont += 1
if n == computador:
    print('\033[1;36mPARABÉNS VOCÊ FOI ÓTIMO!!! ACERTOU DE PRIMEIRA!!\033[m')
while n != computador:
    if computador > n:
        cont += 1
        sleep(1)
        print('Hmmmmm...')
        sleep(1)
        n = int(input('É mais... Qual o seu palpite? '))
    if computador < n:
        cont += 1
        sleep(1)
        print('Hmmmm...')
        sleep(1)
        n = int(input('É menos... Qual o seu palpite? '))
    if n == computador and cont <= 4:
        sleep(1)
        print('Hmmmm...')
        sleep(1)
        print('Parabéns você foi MUITO BOM!!!! E usou apenas \033[m \033[1;33m{}\033[m \033[1;36mtentativas.'.format(cont))
    if n == computador and cont >= 5 and cont < 10:
        sleep(1)
        print('Hmmmm...')
        sleep(1)
        print('Parabéns você acertou! e usou\033[m \033[1;33m{}\033[m \033[1;36mtentativas. Uma nota médiana.'.format(cont))
    if n == computador and cont >= 10:
        sleep(1)
        print('Hmmm...')
        sleep(1)
        print('Olha você acertou, mas foi com\033[m \033[1;33m{}\033[m \033[1;36mtentativas. UMA MÉDIA BEM RUIM...\033[m'.format(cont))
print('\033[1;31m~' * 32, 'FINISH', '\033[1;31m~\033[m' * 30)
#proff ######################################################################################################################################################################
'''from  random import  randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou! com {} tentativas. Prabéns!'.format(palpites))'''


