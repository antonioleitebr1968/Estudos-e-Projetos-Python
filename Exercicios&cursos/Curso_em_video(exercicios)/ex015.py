d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? km'))
preço = (d * 60) + (km * 0.15)
print('Você vai pagar R${:.2f}'.format(preço))

