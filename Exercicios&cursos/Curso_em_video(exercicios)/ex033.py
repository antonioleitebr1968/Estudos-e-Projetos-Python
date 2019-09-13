'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
print('Maior',max(n1, n2, n3))
print('Menor',min(n1, n2, n3))'''
#verificando o menor
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Tarceiro valor: '))
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
