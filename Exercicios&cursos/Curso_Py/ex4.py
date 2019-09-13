'''multiplica = lambda x: x * 2
valor = multiplica(10)
print(valor)

#Função normal
def a(x):
    return x ** 2

b = a(4)
print(b)

#Usando lambda
c = lambda x: x ** 2
e = c(4)
print(e)'''


dobrar = lambda a: a * 2
print(f'O dobro de vinte é: {dobrar(20)}')

somarTudo = lambda *valores: sum(valores)#criado por mim

print(somarTudo(12, 345, 678, 45,))
