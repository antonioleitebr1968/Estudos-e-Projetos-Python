import carro, moto, veiculo, pessoa

uno_vermelho = carro.Carro('vermelho', 'Flex', 1.0, 4)

#help(uno_vermelho.abastecer)
#help(carro.Carro)

uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.acelerar(20)
uno_vermelho.pintar("verde")
print(uno_vermelho.cor)
print(f'A quantidade de combustivel do carro é:')

moto_vermelha = moto.Moto('vermelha', 'Gasolina', 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
moto_vermelha.pintar('azul')

pessoa = pessoa.Pessoa('Jesus')
print(pessoa.nome)

if isinstance(pessoa, veiculo.Veiculo):
    print('é veiculo sim po')
else:
    print('n é veiculo po')

