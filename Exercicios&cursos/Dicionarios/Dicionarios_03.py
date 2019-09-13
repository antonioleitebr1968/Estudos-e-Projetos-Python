## Dicionários parte 3 - Ordenação por chaves; método keys() e função sorted.
# Exemplos:

#Ordenação de dicionarios
d = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
ordenada = list(d.keys())

ordenada.sort()

for key in ordenada:
    print(key, '=', d[key])
print('-=' * 20)
#===============================================
#outra forma

for key in sorted(d):
    print(key, '=', d[key])
