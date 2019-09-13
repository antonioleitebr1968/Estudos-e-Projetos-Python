'''print('=' * 100)
print(' ' *35, 'VAMOS BRINCAR DE JOKENPÔ EEEE')
print('=' * 100)
from random import choice
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)
jogador = str(input('O que você escolhe? ')).strip().upper()
print('Eu escolho {}!'.format(computador))
if computador == 'PEDRA' and jogador == 'PAPEL':
    print('PAPEL ganha de pedra, aaaa eu perdi :(')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('PAPEL GANHA DE PEDRA, HAAAA EU GANHEI!')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('TESOURA CORTA O PAPEL, HAHA EU GANHEI!')
elif computador == 'PAPEL' and jogador == 'TESOURA':
    print('TESOURA corta o papel, aaaa eu perdi :(')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('PEDRA ESMAGA A TESOURA, HAAAAAHAA EU GANHEI!')
elif computador == 'TESOURA' and jogador == 'PEDRA':
    print('PEDRA esmaga a tesoura, aaa eu perdi :(')
elif computador == 'TESOURA' or 'PEDRA' or 'PAPEL' and jogador == 'TESOURA' or 'PEDRA' or 'PAPEL':
    print('O jogo empatou! kaskkask')'''
####################################################################################################################################################
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
cont = 0
computador = randint(0, 2)
faixa = '-=' * 25
titulo = 'BEM VINDO AO JOKENPÔ AUTOMÁTICO!'
print(f'\033[1;30m{faixa}\033[m')
print(f'\033[1;36m{titulo:^50}\033[m')
print(f'\033[1;30m{faixa}\033[m')
print('   ')
while True:
    print('''\033[1;36mSuas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA\033[m''')
    jogador = int(input('\033[1;36mQual é a sua jogada? \033[m'))
    if jogador > 2:
        print('\033[1;35mJOGADA INVÁLIDA.\033[m')
        break
    print('\033[1;36mJO\033[m')
    sleep(0.5)
    print('\033[1;36mKEN\033[m')
    sleep(0.5)
    print('\033[1;36mPÔ!!!\033[m')
    print('\033[1;30m-=\033[m' * 12)
    print('\033[1;36mComputador jogou {}\033[m'.format(itens[computador]))
    print('\033[1;36mJogador jogou {}\033[m'.format(itens[jogador]))
    print('\033[1;30m-=\033[m' * 12)
    if computador == 0:#computador jogou PEDRA
        if jogador == 0:
            print('\033[1;33mEMPATE!!\033[m')
        elif jogador == 1:
            print('\033[1;34mJOGADOR VENCE !!\033[m')
        elif jogador == 2:
            print('\033[1;31mCOMPUTADOR VENCE !!\033[m')
    elif computador == 1:#computador jogou PAPEL
        if jogador == 0:
            print('\033[1;31mCOMPUTADOR VENCE !!\033[m')
        elif jogador == 1:
            print('\033[1;33mEMPATE!!\033[m')
        elif jogador == 2:
            print('\033[1;31mCOMPUTADOR VENCE !!\033[m')
    elif computador == 2:#computador jogou TESOURA
        if jogador == 0:
            print('\033[1;34mJOGADOR VENCE !!\033[m')
        elif jogador == 1:
            print('\033[1;31mCOMPUTADOR VENCE !!\033[m')
        elif jogador == 2:
            print('\033[1;33mEMPATE!!\033[m')
    cont += 1
    if cont == 1:
        break
finish = 'FINISH !!!'
print(f'\033[1;30m{faixa}\033[m')
print(f'\033[1;4;33m{finish:^50}\033[m')




