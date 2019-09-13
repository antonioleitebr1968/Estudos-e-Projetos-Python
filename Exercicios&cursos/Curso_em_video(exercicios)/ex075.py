num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
       int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'O valor "9" apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor "3" foi digitado na {num.index(3) + 1}ª posição')
else:
    print('O valor "3" não foi digitado nenhuma vez')
print('Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

