lista = ('Pão', 1.50, 'Leite', 3.50, 'Açucar', 2.90,
         'Farinha', 2.75, 'Sal grosso', 4.50, 'batata', 25.50,
         'Livros', 52.30, 'Abacaxi', 4.99, 'Carne Perdigão', 24.20)
faixa = '\033[1m-\033[m' * 50
titulo = '\033[1;31mLISTAGEM DE PREÇOS\033[m'
print(faixa)
print(f'{titulo:^60}')
print(faixa)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<40}', end=' ')
    else:
        print(f'R${lista[pos]:.>7.2f}')
print(faixa)