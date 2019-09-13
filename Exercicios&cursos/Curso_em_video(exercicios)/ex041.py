from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc
print('A sua idade é de {} anos'.format(idade))
if idade <= 9:
    print('e sua categoria é MIRIM')
elif idade <= 14:
    print('e sua categoria é INFANTIL')
elif idade <= 19:
    print('e sua categoria é JUNIOR')
elif idade <= 25:
    print('e sua categoria é SÊNIOR')
else:
    print('e sua categoria é MASTER')


