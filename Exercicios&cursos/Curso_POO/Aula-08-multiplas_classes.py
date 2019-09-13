class Animal:
    def __init__(self, cor, genero, andar):# 'self' significa ele mesmo
        self.cor = cor
        self.genero = genero
        self.num_de_patas = andar


    def falar(self):
        print('Olá sou um cahcorro e sei falar')


    def andar(self):
        print(f'Estou andando sobre {self.num_de_patas}')


    def amamentar(self):
        if self.genero.lower()[0] == 'm':
            print('Machos não amamentam')
            return
        print('Amamentando meu filhote')


'''Rex = Animal('Marron', 'Macho', 4)
Rex.falar()
Rex.andar()
Rex.amamentar()'''

class Pessoa(Animal):
    def __init__(self, cor, genero, andar, cabelo):
        super(Pessoa, self).__init__(cor, genero, andar)
        self.cabelo = 'Castanho'

    def falar(self):
        super(Pessoa, self).falar()
        print('Olá sou uma pessoa e sei falar')

Hugo = Pessoa('branco', 'masculino', 2, 'castanho')
Hugo.falar()








