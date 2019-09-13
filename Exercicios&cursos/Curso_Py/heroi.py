class Heroi:
    """
    Classe de heróis
    """

    def __init__(self, voa, lanca_teia, possui_arma, frase_comum):
        self.voa = voa
        self.lanca_teia = lanca_teia
        self.possui_arma = possui_arma
        self.frase_comum = frase_comum

    def falar(self):
        print(self.frase_comum)

    def detalhar(self):
        if self.voa:
            print("O herói voa")
        if self.lanca_teia:
            print("O herói lança teia")
        if self.possui_arma:
            print("O herói possui arma")
