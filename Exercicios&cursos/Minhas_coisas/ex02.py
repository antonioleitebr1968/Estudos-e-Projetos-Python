alturas = list()
idades = list()
cont = 1
for c in range(0, 5):
    a = float(input('Digite a sua altura: '))
    alturas.insert(0, a)
    i = int(input('Digite a sua idade: '))
    idades.insert(0, i)
print('A lista de altura em ordem inversa é: ', end=' ')
for a in alturas:
    print(f'{a:.2f}', end=', ')
print(f'\nA lista da idade em ordem inversa é: ', end=' ')
for i in idades:
    print(i, end=', ')


