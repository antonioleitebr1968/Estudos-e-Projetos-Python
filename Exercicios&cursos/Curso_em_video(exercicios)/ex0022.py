print('='*50, 'Desafio 22', '='*50)
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))#separa em listas o seu nome e conta quantas
# caracteres tem na lista separada.
