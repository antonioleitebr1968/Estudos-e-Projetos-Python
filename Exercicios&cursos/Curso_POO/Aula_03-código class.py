class Meu_Objeto:
    def __init__(pessoa, nome, idade):
        pessoa.nome = nome
        pessoa.idade = idade
        print('Chamando o construtor')


    def imprime(pessoa):
        print(f'Olá meu nome é {pessoa.nome} e eu tenho {pessoa.idade}')


Hugo = Meu_Objeto('Hugo', 27)

Hugo.imprime()
