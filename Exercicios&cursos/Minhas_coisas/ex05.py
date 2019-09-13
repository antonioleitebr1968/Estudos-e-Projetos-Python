#Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
lista1 = list()
lista2 = list()
titulo1 = 'Primeira lista'
titulo2 = 'Segunda lista'
print('-=' * 30)
print(f'{titulo1:^60}')
for c in range(0, 10):
    num = int(input('Digite um número: '))
    lista1.append(num)
print('-=' * 30)
print(f'{titulo2:^60}')
for c in range(0, 10):
    n = int(input('Digite um valor: '))
    lista2.append(n)
print('-=' * 30)
print(f'O resultado das duas listas com seus respectivos elementos é: {lista1 + lista2}')
