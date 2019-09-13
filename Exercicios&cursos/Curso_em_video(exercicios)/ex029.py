velocidade = float(input('Digite a velocidade do seu carro: '))
if velocidade > 80:
    print('Você foi multado em R${:.2f} porque ultrapassou o limite de 80km/h.'.format((velocidade-80) * 7))
else:
    print('Ok! sua velocidade esta dentro do limite permitido!')


