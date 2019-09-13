# Exemplo 01
'''d1 = {}#dicionario
d1['aaa'] = 100#adicionando item ao dicionario
print(d1)'''#imprimindo o dicionario
# Exemplo 02
'''b = [1, 2, 3]
a = {'c': 1000, 'd': 10, 20: b}#dicionario com lista dentro
print(f'{a[20][2]}')#com a chave 20 estou buscando na lista "b"(QUE É UM VALOR), o valor "3" que tambem é um valor'''
# Exemplo 03
a = {'x': 35, 'v': 45, 'b': 20}
print(a.keys())# retorna a lista de chaves
print(a.values())# retorna a lista de valores
print(a.get('x'))# retorna o valor da chave 'x'
#--------------------------------------------------------------------------
print(a.popitem())# retorna e remove um elemento aleatorio do dicionario
print(a)
#--------------------------------------------------------------------------
print('X' in a)# pergunta se a chave está contida dentro do dicionario
t = (10, 10, 10)# tupla
a[t] = 'eXcript'# Relacionando essa cadeia de caracteres a tupla "t", ou seja definindo uma tupla como chave.
print(a)
#  OBS: no caso de listas isso n da certo pois as listas são mutaveis





