#variáveis compostas(LISTAS) -------------------------------------------------------------
#OBERVAÇÕES: LISTAS SÃO MUTÁVEIS DIFERENTE DAS TUPLAS.
#EXEMPLO 1 -------------------------------------------------------------------------------
num = [2, 5, 9, 1]
num[2] = 3
print(num)
#exemplo a cima mostrando que listas são mutaveis

#EXEMPLO 2 ----------------------------------------
#adicionando o valor "7" na lista
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)#esse metódo adiciona o valor "7" na ultima posição da lista
num.sort()#esse metódo coloca em ordem crescente
num.sort(reverse=True)# esse metódo coloca em ordem decrecente
num.insert(2, 0)# esse metódo adiciona o valor "0" na posição desejada da lista, que nesse caso é na posição 2
num.pop()# esse comando remove o último elemento da lista
num.pop(2)#esse comando remove o elemento na posição "2" da lista
num.remove(2)# esse comando remove o primeiro valor "2" que encontrar
print(num)
print(f'Essa lista tem {len(num)} elementos')

#EXEMPLO 3 ---------------------------------------------------------------------------------------------------------
#mostrando a lista de maneira bonitinha
valores = list()# criando uma lista vazia
valores.append(5)
valores.append(9)
valores.append(4)
#---------------------------------------------------------------------------------
#for v in valores:#metódo para mostrar de maneira bonitinha
    #print(f'{v}...', end=' ')
#---------------------------------------------------------------------------------
#exemplo 3 -----------------------------------------------------------------------
#além do valor ele mostra o indice
for c, v in enumerate(valores):# na posição "c" ele mostra os valores
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
#exemplo 4 -----------------------------------------------------------------------
valores = list()
for cont in range(0, 5):#lendo valores pelo teclado e colocando dentro da lista
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):# na posição "c" ele mostra os valores
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
#EXEMPLO 5 -----------------------------------------------------------------------

a = [2, 3, 4, 7]
b = a#OBS: ATENÇÃO ISSO AQUI FAZ UMA LIGÇÃO ENTRE UMA LISTA E OUTRA E NÃO ESTA FAZENDO UMA COPIA
b[2] = 8#exemplo provando a observação a cima
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#EXEMPLO 6 ---------------------------------------------------------------------------------------
#AGORA SIM FAZENDO UMA COPIA
c = [2, 3, 4, 7]
d = c[:]#criando uma copia da lista
d[2] = 8
print(f'Lista A: {c}')
print(f'Lista B: {d}')
