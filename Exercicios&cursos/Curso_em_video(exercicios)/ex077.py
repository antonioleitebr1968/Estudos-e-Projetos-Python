palavras = ('bola', 'aprender', 'lista', 'carro', 'moto', 'bicicleta',
            'fome', 'analfabeto', 'triste', 'feliz', 'chora', 'nenem')
for p in palavras:
    print(f'\nNa palavra \033[1;31m{p.upper()}\033[m temos as seguintes vogais: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[1;36m{letra}\033[m', end=' ')

