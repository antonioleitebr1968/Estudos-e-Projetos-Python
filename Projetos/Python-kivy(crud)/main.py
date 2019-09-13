import cliente, cliente_repositorio

'''
cliente1 = cliente.Cliente('Lucas', 25)
cliente2 = cliente.Cliente('Antonio', 34)
cliente3 = cliente.Cliente('Ramon', 60)
cliente4 = cliente.Cliente('Talita', 12)
cliente5 = cliente.Cliente('Renata', 15)
cliente6 = cliente.Cliente('jubileu', 55)
cliente7 = cliente.Cliente('Romeu', 36)
cliente8 = cliente.Cliente('Julieta', 35)
cliente9 = cliente.Cliente('Bernardo', 22)


lista_de_clientes = [(cliente1.nome, cliente1.idade),
                     (cliente2.nome, cliente2.idade),
                     (cliente3.nome, cliente3.idade),
                     (cliente4.nome, cliente4.idade),
                     (cliente5.nome, cliente5.idade),
                     (cliente6.nome, cliente6.idade),
                     (cliente7.nome, cliente7.idade),
                     (cliente8.nome, cliente8.idade),
                     (cliente9.nome, cliente9.idade)]
'''

#cliente0 = cliente.Cliente("João", 29)


print(cliente_repositorio.ClienteRepositorio.listar_clientes())
#cliente_repositorio.ClienteRepositorio.inserir_cliente(cliente1)
#cliente_repositorio.ClienteRepositorio.editar_cliente(3, cliente0)
#cliente_repositorio.ClienteRepositorio.remover_cliente(6)

#cliente_repositorio.ClienteRepositorio.inserir_varios_cliente(lista_de_clientes)
