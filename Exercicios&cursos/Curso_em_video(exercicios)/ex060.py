#exemplo 1 --------------------------------------------------------
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''
#exemplo 2 --------------------------------------------------------
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n), end=' = ')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))'''
#exemplo 3 com for ------------------------------------------------
n = int(input('Digite um número para calcular seu Fatorial: '))
print('Calculando {}!'.format(n), end=' ')
f = 1
for c in range(0, n):
    fac = n - c
    print('{}'.format(fac), end=' ')
    print('x' if fac > 1 else '=', end=' ')
    f *= fac
print('{}'.format(f))



