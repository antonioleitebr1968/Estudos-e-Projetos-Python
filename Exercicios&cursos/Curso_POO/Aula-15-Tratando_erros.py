#Exemplo 1
'''try:
    x = int(input('Digite um número: '))
except:
    print('Deu erro, insira apenas números')
    x = 0
print(x)'''

#Exemplo 2

class ValorRepetidoErro(Exception):

    def __init__(self, n):
        self.num = n

    def __str__(self):
        return f'Vixe Você já digitou esse valor {self.num} antes'

def main():
    lista = []
    for i in range(8):
        while True:
            try:
                num = int(input('Digite um número: '))
                break
            except ValueError:
                print('Digite apenas números')
        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)


main()
