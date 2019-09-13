r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos a cima podem SIM formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')#TODOS OS LADOS IGUAIS
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')##TODOS OS LADOS DIFERENTES
    else:
        print('ISÓSCELES')#DOIS LADOS IGUAIS
else:
    print('Os seguimentos a cima NÃO podem formar um triângulo!')
