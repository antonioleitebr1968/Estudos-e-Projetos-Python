#método 1
'''s = float(input('Qual o valor do seu sálario? '))
if s > 1.250:
    salario = s + (s * 10 / 100)
if s <= 1250:
    salario = s + (s * 15 / 100)
print(salario)'''
#método 2
s = float(input('Qual é o valor do seu sálario? R$'))
if s > 1250:
    print('Seu sálario ficará R${:.2f} com 10% de aumento!'.format(s + (s * 10 / 100)))
if s <= 1250:
    print('Seu sálario ficará R${:.2f} com 15% de aumento!'.format(s + (s * 15 / 100)))


