#progressão aritmética
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão#formula para calcular a progressão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('ACABOU')

