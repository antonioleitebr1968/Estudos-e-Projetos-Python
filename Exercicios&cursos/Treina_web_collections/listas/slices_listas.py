lista_simples_inteiro = [1, 2, 8, 4, 5, 14]

nova_lista = lista_simples_inteiro[0:4]
print(nova_lista)
print(lista_simples_inteiro[1:])
print(lista_simples_inteiro[:3])
print(lista_simples_inteiro[1::2])

intervalo = slice(1, 4)
print(lista_simples_inteiro[intervalo])
