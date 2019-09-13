'''Exemplo de classes (self) e (__init__).'''
'''# EXEMPLO 01
class chatbot(): # definindo classe
    def __init__(self, nome):# Nota: toda função dentro de classe tem o (self). o (__init__)
        # serve como uma função especial, a primeira que vai ser executada dentro da classe
        self.nome = nome# self serve como um indentificador, ele indentifica a variável que eu atribui o (chatbot)


    def fala(self):
        print('Oi, meu nome é ' + self.nome)

a = chatbot('Eduardo')# atribuindo a variável uma classe. (chatbot)
a.fala()

b = chatbot('Alfredo')
b.fala()'''
# EXEMPLO 02
