'''Crie um programa onde o usuário possa digitar
sete valores numéricos e cadastre-os em uma
lista única que mantenha separdos os valores
pares e ímpares. No final, mostre os valores pares
e ímpares em ordem crescente.'''

'''listagem = list()
pares = list()
impares = list()
for c in range(0, 7):
    num = int(input(f'Digite {c + 1}º valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
listagem.append(pares[:])
listagem.append(impares[:])
listagem = listagem.sort()
print('-=' * 25)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')'''

# proff -----------------------------------------------------
núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')
