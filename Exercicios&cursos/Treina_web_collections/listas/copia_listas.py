import copy
nested_list = [[1, 2], ['ola', 'mundo']]

# Deep Copy
nova_lista = copy.deepcopy(nested_list)
nested_list[0][1] = 'a'
print(nova_lista)
print(nested_list)

# Shallow Copy
outra_lista = copy.copy(nested_list)
nested_list[0][1] = 'b'
print(outra_lista)
print(nested_list)

#meu jeito
#nova_lista2 = nested_list[:]
#print(nova_lista2)