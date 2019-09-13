from random import choice
from palavras import palavra_secreta

class Jogo(object):
    def __init__(self):
        self.__palavraSecreta = ''
        self.__letrasDescobertas = []
        self.__acertou = False
        self.gerarPalavra()

    def gerarPalavra(self):
        self.__palavraSecreta = choice(palavra_secreta)

        for i in self.__palavraSecreta:
            self.__letrasDescobertas.append('-')


    def __compararPalavras(self, descoberta, secreta):
        if descoberta == secreta:
            self.__acertou = True

    def __receberLetra(self, letra):
        for i in range(0, len(self.__palavraSecreta)):
            if letra == self.__palavraSecreta[i]:
                self.__letrasDescobertas[i] = letra

    def jogar(self, entrada):
        if self.__acertou == False:
            #u = str(input('aaaaaaa'))
            ls = entrada
            self.__receberLetra(ls)
            self.mostrarLetrasDescobertas()
            self.__compararPalavras(self.__letrasDescobertas, self.__palavraSecreta)

    def mostrarLetrasDescobertas(self):
        palavra = ''

        for i in self.__letrasDescobertas:
            palavra += i
        print(self.__letrasDescobertas)
        print(self.__palavraSecreta)
        return palavra

    def contarPalavras(self, cont):
        cont += 1
