# Exemplo 1
'''numeros = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 4):
        numeros[i][j] = float(input('Digite um número: '))

print(numeros[0][0])
print(numeros[2][3])'''
# Exemplo 2
original = [[0, 0, 0],
            [0, 0, 0]]

trasnposta = [[0, 0],
              [0, 0],
              [0, 0]]

for i in range(0, 2):
    for j in range(0, 3):
        original[i][j] = float(input('Digite: '))

for i in range(0, 2):
    for j in range(0, 3):
        trasnposta[j][i] = original[i][j]
print(original)
print(trasnposta)

