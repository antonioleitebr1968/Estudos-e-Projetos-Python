d = float(input('Digite a distância da sua viagem: '))
if d <=200:
    print('O valor da sua passagem é R${:.2f}'.format(d * 0.50))
else:
    print('O valor da sua passagem é R${:.2f}'.format(d * 0.45))
#condição simplificada a baixo:
'''distancia = float(input('Qual é a distância da sua viagem? '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(preço))'''

