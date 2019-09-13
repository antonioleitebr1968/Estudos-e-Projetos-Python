#AULA SOBRE TUPLAS / OBDS:  AS TUPLAS SÃO IMUTAVÉIS.

#exemplo 1
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')# isso é uma tupla (uma váriavél composta)
print(lanche)



#exemplo de tupla com fatiamento (relembrando: no fatiamento o ultimo elemento é ignorado
print(lanche[0])
print(lanche[2:])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-1])# fatiamento de trás pra frente
print(lanche[-2])
print(lanche[-2:])# começa da pizza e vai até o final
print(lanche[-3])

#exemplo de que tuplas são imutavéis
#lanche[1] = 'Refrigerante' #exemplo comprovando que tuplas são imutavéis

#exemplo 3 (com for) obs: estrutura de repetição
for comida in lanche:# significado do 'for' : "para cada comida em lanche"
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

#exemplo 4
lanche1 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(len(lanche)) #mostra a quantidade de itens na tupla
for cont in range(0, len(lanche1)):
    print(f'Eu vou comer {lanche1[cont]}')# exemplo de como mostrar a tupla
print('Comi pra caramba!')
#OBS OS DOIS EXEMPLOS FOR A CIMA MOSTRAM A MESMA COISA SÓ QUE UM UTILIZANDO O 'RANGE' E O OUTRO UTILIZANDO DIRETO A VARIAVÉL COMPOSTA "LANCHE"

#exemplo 5 mostrando a posição
lanche1 = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche1)):
    print(f'Eu vou comer {lanche1[cont]} na posição {cont}')# mostrando o que vai comer em tal posição
print('Comi pra caramba!')

#exemplo 6 mostrando a posição (mostra exatamente a mesma coisa do exemplo 5)
for pos, comida in enumerate(lanche1):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

#exemplo 7
print(sorted(lanche1))# esse exemplo coloca a tupla em ordem

#exemplo 8 (mais exemplos de tuplas)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # essa forma junta uma tupla com a outra
print(c)
#exemplo 9
print(len(c))# me mostra quantos elementos tem na tupla "c" que é a junção das tuplas "a" e "b"
print(c.count(5))# isso mostra quantas vezes está aparecendo o número "5" dentro da tupla "c"
print(c.index(2))# mostra em que posição está o "2"
print(c.index(5, 1))# mostra em que posição está o 5 começando da posição 1 (isso é o que a gente chama de deslocamento)

#exemplo 10
pessoa = ('Matheus', 19, 'M', 50.00)
#del(pessoa) #apagando uma váriavel e também uma tupla
print(pessoa)
