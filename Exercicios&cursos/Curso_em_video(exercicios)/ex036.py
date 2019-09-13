print('\033[1;35m-~~-\033[m' * 26)
print('\033[1;34mÓla, seja bem vindo ao nosso programa!\n ele tem como função te falar se você está apto para fazer o empréstimo,\n e enfim comprar a sua casa própria :)\033[m')
print('\033[1;35m-~~-\033[m' * 26)
casa = float(input('\033[1;36mQual é o valor da casa? R$\033[m'))
sálario = float(input('\033[1;36mQual é o valor do seu sálario? R$\033[m'))
anos = int(input('\033[1;36mEm quantos anos quer pagar? \033[m'))
prestação = casa / (anos * 12)
mínimo = sálario * 30 / 100
print('\033[1;36mPara pagar uma casa de\033[m \033[1;31;43mR${:.2f}\033[m \033[1;36mem {} anos'.format(casa, anos), end=' ')
print('a prestação será de\033[m \033[1;31;43mR${:.2f}\033[m'.format(prestação))
if prestação <= mínimo:
    print('\033[1;34mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')
print('\033[1;35m-~~-\033[m' * 26)
print(' ' * 44, '\033[1;31mFINISH!\033[m')
print('\033[1;35m-~~-\033[m' * 26)