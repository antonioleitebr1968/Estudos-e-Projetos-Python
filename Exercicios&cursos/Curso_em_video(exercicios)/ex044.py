print('-=-' * 40)
print(' ' * 40 ,'Gerenciador de Pagamentos')
print('-=-' * 40)
preço = float(input('Qual o preço das compras? R$'))
opção1 = preço - (preço * 10 / 100)
opção2 = preço - (preço * 5 / 100)
opção3 = preço
opção4 = preço + (preço * 20 / 100)
print('Por favor escolha uma opção:')
print('''OPÇÃO [ 1 ] 10% de desconto no dinheiro ou cheque.
OPÇÃO [ 2 ] á vista no cartão com 5% de desconto.
OPÇÃO [ 3 ] em até 2x no cartão, preço normal.
OPÇÃO [ 4 ] 3x ou mais no cartão com 20% de juros.''')
escolha = int(input('Digite a OPÇÃO aqui >>> '))
if escolha == 1:
    print('O preço de {:.2f} ficará {:.2f} com 10% de desconto, no dinheiro ou cheque.'.format(preço, opção1))
elif escolha == 2:
    print('O preço de {:.2f} ficará {:.2f} com 5% de desconto, á vista no cartão.'.format(preço, opção2))
elif escolha == 3:
    print('O preço de {:.2f} se mantem o mesmo em até 2x no cartão.'.format(opção3))
elif escolha == 4:
    print('O preço de {:.2f} ficará {:.2f} com 20% de juros em 3x ou mais no cartão.'.format(preço, opção4))
else:
    print('Por favor escolha uma opção válida')



