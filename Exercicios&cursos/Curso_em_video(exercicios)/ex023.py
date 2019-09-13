num = int(input('Digite um número inteiro de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A sua unidade é {}'.format(u))
print('A sua Dezena é {}'.format(d))
print('A sua centena é {}'.format(c))
print('A sua Milhar é {}'.format(m))