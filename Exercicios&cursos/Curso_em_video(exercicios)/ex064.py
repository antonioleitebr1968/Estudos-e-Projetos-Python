#minha solução --------------------------------------------------------------
'''print('Digite [ 999 ] para fechar o programa')
soma = 0
cont = 0
sair = False
while not sair:
    num = int(input('Digite um número inteiro: '))
    cont += 1
    if num == 999:
        sair = True
    soma += num
print('Foram {} números digitados'.format(cont - 1), end=' ')
print('e a soma entre eles foi de {}'.format(soma - 999))
print('~' * 50)
print(' ' * 14, 'PROGRAMA FINALIZADO')
print('~' * 50)'''
#prof ------------------------------------------------------------------------
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
