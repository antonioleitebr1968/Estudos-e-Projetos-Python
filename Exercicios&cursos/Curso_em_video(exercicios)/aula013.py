'''for c in range(0, 7, 2):# conta de 0 a 7 pulando de dois em dois
    print(c)
print('FIM')
for c in range(1, 6):#conta de 1 até 5 pq o 6 n conta
    print(c)
print('FIM')
for c in range(0, 6):#no lugar do (c) tbm pode usar uma string dentro de aspas
    print(c)
print('FIM')
for c in range(6, 0, -1):#ele conta pra trás
    print(c)
print('FIM')'''
'''n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')'''
''''#digita um número e ele vai contar do inicio ao fim pulando utilizando o passo
i =int(input('Início: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''
s = 0
for c in range(0, 4):
    n = int(input('digite um valor: '))
    s += n#igual a: s = s + n
print('O somatório de todos os valores foi {}'.format(s))
