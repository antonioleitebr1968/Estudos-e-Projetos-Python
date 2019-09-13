## Dicionários parte 2 - Aninhamento de Dicionários e Listas; Inclusão de valores
#Exemplos:

r = {'nome': {'primeiro': 'Matheus',
              'sobrenome': 'Morais'},
     'conhecimentos': ['Python', 'ensino médio'],
     'idade': 19}

print('{}'.format(r['conhecimentos'][0]))
print('{}'.format(r['conhecimentos'][1]))
print('{}'.format(r['conhecimentos'][-1]))#retorna o ultimo elemento da lista
print('{}'.format(r['idade']))
print('{}'.format(r['nome']['primeiro']))
print('{}'.format(r['nome']['sobrenome']))
r['conhecimentos'].append('Futuro ADS')#adicionando item a lista do dicionario, chave conhecimentos
print('{}'.format(r['conhecimentos'][-1]))
