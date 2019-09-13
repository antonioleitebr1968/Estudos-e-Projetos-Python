import abc, interface_veiculo

class Veiculo(abc.ABC):
    """Essa é a classe carro, esta classe é utilizada para instanciar novos
carros em nosso programa"""
    def __init__(self, cor, tipo_combustivel, potencia):

        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memoria. :)")

    @property
    def cor(self):
        return self._cor

    def pintar(self, cor):
        self._cor = cor

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parâmetro a quantidade de combustivel
 e incrementa no atribulto self.qtd_combustivel do carro"""
        self.__qtd_combustivel += qtd_combustivel

    def ligar(self):

        if self.__is_ligado:
            print('O veiculo já está ligado')
        else:
            self.__is_ligado = True
            print('O veiculo foi ligado')

    def desligar(self):

        if self.__is_ligado:
            self.__is_ligado = False
            print('O veiculo foi desligado')
        else:
            print('O veiculo já está desligado')

    def acelerar(self, velocidade = 10):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print('ligue o veiculo primeiro né sua mula')
