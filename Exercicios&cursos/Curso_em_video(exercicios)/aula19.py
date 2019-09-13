#Exemplo 01 ======================================================

"""pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())#mostra todas as chaves
print(pessoas.values())#mostra todas os valores
print(pessoas.items())#mostra todas as chaves e valores"""

#Exemplo 02 ======================================================

"""pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 22}
for k in pessoas.keys():
    print(k)
print('-' * 15)
for v in pessoas.values():
    print(v)
print('-' * 15)
for k, v in pessoas.items():
    print(f'A chave é {k} e o valor é {v}')"""


#Exemplo 03 =======================================================
#apagando uma chave com valor
"""pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 22}
print(pessoas)
del pessoas['sexo']#metodo que apaga
print(pessoas)"""

#Exemplo 04 =======================================================

#trocando um valor da chave
"""pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 22}
print(pessoas)
pessoas['nome'] = 'Leo'
print(pessoas)"""

#Exemplo 05 =======================================================

#adicionando elemento ao dicionario
"""pessoas = {'nome': 'Matheus', 'sexo': 'M', 'idade': 22}
print(pessoas)
pessoas['peso'] = 55.6
print(pessoas)"""

#Exemplo 06 =======================================================

#Criando dicionario dentro de uma lista

"""brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])"""

#Exemplo 07 ========================================================

#fazendo uma copia e outras coisinhas
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())#copia
print(brasil)
print('-' * 30)
for e in brasil:
    print(e)
print('-' * 30)
#mostrando bonitinho
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print('-' * 30)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
print()
print('-' * 30)
for e in brasil:
    for k in e.keys():
        print(k, end=' ')
print()
print('-' * 30)

















