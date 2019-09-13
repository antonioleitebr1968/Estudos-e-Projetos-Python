'''print('#' * 100)
print(' ' * 10, 'Digite o ano em que você nasceu para saber se esta na hora de se alistar!')
print('#' * 100)
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
print('#' * 100)
print(' ' * 44, 'Finish!')
print('#' * 100)'''
#################################################################################################################################################
print('\033[1;34m#\033[m' * 100)
print(' ' * 10, '\033[1;31mDigite o ano em que você nasceu para saber se esta na hora de se alistar!\033[m')
print('\033[1;34m#\033[m' * 100)
from datetime import date
atual = date.today().year
sexo = str(input('\033[1;33mMas antes, você é de sexo masculino ou feminino? \033[m')).strip().lower()
if sexo == 'masculino':
    print('\033[1;33mOk começaremos o processo...\033[m')
    print('\033[1;31m----------------------------------------------------------------------------------------------------\033[m')
    nasc = int(input('\033[1;33mAno de nascimento? \033[m'))
    idade = atual - nasc
    print('\033[1;33mQuem nasceu em {} tem {} anos em {}\033[m'.format(nasc, idade, atual))
    if idade == 18:
        print('\033[1;33mVocê tem que se alistar\033[m \033[1;31mIMEDIATAMENTE!\033[m')
    elif idade < 18:
        saldo = 18 - idade
        print('\033[1;33mAinda faltam {} anos para o alistamento!\033[m'.format(saldo))
        ano = atual + saldo
        print('\033[1;33mSeu alistamento será em\033[m \033[1;36m{}\033[m'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('\033[1;33mVocê já deveria ter se alistado há\033[m \033[1;31;40m{}\033[m \033[1;33manos!\033[m'.format(saldo))
        ano = atual - saldo
        print('\033[1;33mSeu alistamento foi em\033[m \033[1;31;40m{}\033[m'.format(ano))
elif sexo == 'feminino':
    print('\033[1;36mMulheres não precisam passar por o processo de alistamento!\033[m')
else:
    print('\033[1;33mPor favor digite apenas "masculino" ou "feminino"\033[m')
print('\033[1;34m#\033[m' * 100)
print(' ' * 44, '\033[1;31mFinish!\033[m')
print('\033[1;34m#\033[m' * 100)
