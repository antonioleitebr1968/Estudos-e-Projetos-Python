faixa = '-=' * 50
finish = 'FINISH'
primeira = str(input('\033[1;36mPrimeira string: '))
segunda = str(input('Segunda string: \033[m'))
print(f'\033[1;30m{faixa}\033[m')
if len(primeira) == len(segunda):
    print('\033[1;36mAs duas strings tem o mesmo tamanho\033[m')
print(f'\033[1;36mA primeira string digita foi "{primeira}" com o comprimento de {len(primeira)} caracteres.\033[m')
if ' ' in primeira:
    print(f'\033[1;36mE tem {len(primeira) - primeira.count(" ")} caracteres sem espaços.\033[m')
print(f'\033[1;30m{faixa}\033[m')
print(f'\033[1;36mA segunda string digita foi "{segunda}" com o comprimento de {len(segunda)} caracteres.\033[m')
if ' ' in segunda:
    print(f'\033[1;36mE tem {len(segunda) - segunda.count(" ")} caracteres sem espaços.\033[m')
print(f'\033[1;30m{faixa}\033[m')
print(f'\033[1;33m{finish:^100}\033[m')






