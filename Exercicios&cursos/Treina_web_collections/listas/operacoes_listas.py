lista_simples_inteiro = [1, 2, 8, 4, 5, 14, 3, 3]
lista_simples_strings = ['Olá', 'mundo']
lista_mesclada = [1, 2.2, 'aaaa', True]
nested_list = [[1, 2], ['ola', 'mundo']]

print(lista_simples_inteiro)
print(nested_list)

#len()
print(len(lista_mesclada))
print(len(nested_list))

#append()
lista_simples_inteiro.append(6)
print(lista_simples_inteiro)

#insert()
#lista_simples_inteiro.insert(2, "haha")
#print(lista_simples_inteiro)

#remove()
lista_simples_inteiro.remove(1)
print(lista_simples_inteiro)

#index()
index = lista_simples_inteiro.index(3)
print(index)

#count()
count = lista_simples_inteiro.count(3)
print(count)

#sort()
lista_string = ['a', 'c', 'b']
lista_simples_inteiro.sort(reverse=True)
lista_string.sort(reverse=False)
print(lista_simples_inteiro)
print(lista_string)
print('=' * 40)