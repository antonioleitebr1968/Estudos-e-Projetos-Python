peso = float(input('Qual o peso da pessoa? (kg) '))
altura = float(input('Qual a altura da pessoa? (m) '))
massa = peso / altura ** 2
print('Sua massa corporal é de {:.1f}'.format(massa), end=' ')
if massa < 18.5:
    print('e você está abaixo do peso!')
elif massa >= 18.5 and massa < 25:#exemplo simplificado: elif <= 18.5 massa < 25:
    print('e você está no peso ideal!')
elif massa >= 25 and massa < 30:
    print('e você está com sobrepeso!')
elif massa >= 30 and massa < 40:
    print('e você está com obesidade!')
else:
    print('e você está com obesidade mórbida!')
