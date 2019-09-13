from time import sleep
v1 = int(input('Digite um valor: '))
v2 = int(input('Outro valor: '))
sair = False
while not sair:
    print('[ 1 ] para somar')
    print('[ 2 ] para multiplicar')
    print('[ 3 ] para ver o maior')
    print('[ 4 ] para novos números')
    print('[ 5 ] para sair do programa')
    opção = int(input('>>>>>> Qual é sua opção? '))
    if opção == 5:
        sair = True
    elif opção == 4:
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Outro valor: '))
    elif opção == 3:
        if v1 == v2:
            print('não existe maior, os dois valores são iguais')
        if v1 > v2:
            maior = v1
            print('O Maior número é {}'.format(maior))
        elif v2 > v1:
            maior = v2
            print('O Maior é número {}'.format(maior))
    elif opção == 2:
        m = v1 * v2
        print('O resultado da multiplicação entre os dois números é {}'.format(m))
    elif opção == 1:
        somar = v1 + v2
        print('A soma dos números é {}'.format(somar))
    else:
        print('Por favor digite uma opção valida.')
    print('-==-' * 20)
    sleep(2)
print('Programa finalizado')


