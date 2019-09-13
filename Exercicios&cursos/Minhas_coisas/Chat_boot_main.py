'''def Chat_Boot_Goku():'''

# funções ============================================================================================================
def advinhação():
    from time import sleep
    from random import randint
    computador = randint(0, 10)
    cont = 0
    n = int(input('\033[1;36mOk! vou pensar em um número de 0 a 10... Em que número eu pensei? '))
    cont += 1
    if n == computador:
        print(f'\033[1;36mPARABÉNS VOCÊ FOI ÓTIMA Milena!!! ACERTOU DE PRIMEIRA!!\033[m')
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
            print(f'''Parabéns você foi MUITO BOA!!!! 
E usou apenas \033[m \033[1;33m{cont}\033[m \033[1;36mtentativas.''')
        if n == computador and cont >= 5 and cont < 10:
            sleep(1)
            print('Hmmmm...')
            sleep(1)
            print(f'''Parabéns você acertou!
E usou\033[m \033[1;33m{cont}\033[m \033[1;36mtentativas. Uma nota médiana, Milena.''')
        if n == computador and cont >= 10:
            sleep(1)
            print('Hmmm...')
            sleep(1)
            print(f'''Olha Milena você acertou, 
mas foi com\033[m \033[1;33m{cont}\033[m \033[1;36mtentativas. UMA MÉDIA BEM RUIM...\033[m''')
# -------------------------------------------------------------------------------------------------------------
def jokenpô():
    from random import randint
    from time import sleep
    itens = ('Pedra', 'Papel', 'Tesoura')
    cont = 0
    Goku = randint(0, 2)
    faixa = '-=' * 25
    titulo = 'Ok Milena vamos começar!!!'
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
            print(f'\033[1;35mAhhh poxa Milena você não sabe jogar...\033[m')
            break
        print('\033[1;36mJO\033[m')
        sleep(0.5)
        print('\033[1;36mKEN\033[m')
        sleep(0.5)
        print('\033[1;36mPÔ!!!\033[m')
        print('\033[1;30m-=\033[m' * 12)
        print(f'\033[1;36mGoku jogou {itens[Goku]}\033[m')
        print(f'\033[1;36mMilena jogou {itens[jogador]}\033[m')
        print('\033[1;30m-=\033[m' * 12)
        if Goku == 0:  # computador jogou PEDRA
            if jogador == 0:
                print('\033[1;33mEMPATE!!\033[m')
            elif jogador == 1:
                print('\033[1;34mah poxa você venceu !\033[m')
            elif jogador == 2:
                print('\033[1;31mHAAA VENCI !!\033[m')
        elif Goku == 1:  # computador jogou PAPEL
            if jogador == 0:
                print('\033[1;31mHAAA VENCI !!\033[m')
            elif jogador == 1:
                print('\033[1;33mEMPATE!!\033[m')
            elif jogador == 2:
                print('\033[1;31mHAAA VENCI !!\033[m')
        elif Goku == 2:  # computador jogou TESOURA
            if jogador == 0:
                print('\033[1;34mah poxa você venceu !\033[m')
            elif jogador == 1:
                print('\033[1;31mah poxa você venceu !\033[m')
            elif jogador == 2:
                print('\033[1;33mEMPATE!!\033[m')
        cont += 1
        if cont == 1:
            break




# ====================================================================================================================

from random import randint
print('Oi eu sou o Goku!', end=' ')
conhecidos = ['Nathan', 'Felipe', 'Edson']
especial = 'Milena'
especial2 = 'Matheus'
nome = str(input('e você? ')).strip().capitalize()
if nome == especial:
    escolhendo_resposta = randint(1, 3)
    if escolhendo_resposta == 1:
        print('''Aaaa eu sei quem é você! é a namorada do Matheus!
ele fala bastante de você, ele sempra fala que você é como uma semente dos Deuses para ele! rs''')
    if escolhendo_resposta == 2:
        print('''Nossa a namorada do Matheus! muito prazer senhorita,
ele sempre fala muito bem de você!''')
    elif escolhendo_resposta == 3:
        print('''Eita a namorda do Matheus!, ele fala que você é muito divertida!
Bem vamos ver isso!''')
if nome == especial:
    resposta1_especial = str(input(f'Quer brincar comigo {nome}? ')).strip().upper()[0]
    if resposta1_especial == 'S':
        resposta2_especial = int(input('''Quer brincar de advinhação ou jokenpô?
[ 1 ] para advinhação e [ 2 ] para jokenpô: '''))
        if resposta2_especial == 1:
            advinhação()
        if resposta2_especial == 2:
            jokenpô()
    if resposta1_especial == 'N':
        print('continua...')
if nome in conhecidos:
    resp1 = str(input('Eaiii como vai? tudo bem? ')).strip().upper()[0]
    if resp1 == 'S':
        resp2 = str(input('Ah que bom deseja brincar comigo? ')).strip().upper()[0]
        if resp2 == 'S':
            print('jogo')# A função de jogo deverá ser aplicada aqui


#continua depois...



