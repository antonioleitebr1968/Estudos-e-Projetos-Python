#so pra n esquecer e tals
'''n = cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1'''
# exemplo 1, mais exemplo da atualização do print--------------------------------------------------------------------
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')#novo metodo

#mais exemplo do print

nome = 'josé'
idade = 33
salário = 987.30
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}.')
#xemplos print
#{nome:^20} alinhar
#{nome:^-20} alinhar complemento
#{nome:^20} alinhar
#{nome:->20} alinhar complemento a direita
#{nome:-<20} alinhar complemento a esquerda
#exemplo para centralizar com sinais do lado
#print('{:-^40}'.format('Fim do programa'))