#print('exemplo 1')
#print('=' * 50, 'Exemplo 1', '=' * 50)
#tempo = int(input('Quantos anos seu carro tem? '))
#if tempo <= 3:
#    print('carro novo')
#else:
#    print('carro velho')
#print('-' * 50, 'FIM', '-' * 50)
#print('exemplo 2')
#nome = str(input('Qual é o seu nome? '))
#if nome =='Matheus':
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é tão normal!')
#print('Bom dia, {}!'.format(nome))
print('exemplo 3')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')