import veiculo

class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print('O método foi chamado a partir da classe Moto')
        if self._qtd_combustivel >= 30:
            print('O tanque da moto ta cheio doido')
        else:
            self._qtd_combustivel += qtd_combustivel

    def pintar(self, cor):
        if cor == 'azul':
            print('nananinanão')
        else:
            self._cor = cor
