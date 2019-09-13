print('====================DESAFIO 05====================')
n1 = int(input('Digite um valor inteiro'))
s = n1 + 1
s1 = n1 - 1
print('O seu número sucessor é {}, e o seu antecessor é {}'.format(s,s1))
print('====================DESAFIO 06====================')
n2 = int(input('Digite um número inteiro'))
s2 = n2 * 2
s3 = n2 * 3
s4 = n2 ** (1/2)
print('O seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.2f}'.format(s2, s3, s4))
print('====================DESAFIO 07====================')
n3 = float(input('Digite uma nota'))
n4 = float(input('Digite outra nota'))
s5 = (n3 + n4) / 2
print('A sua média é {:.1f}'.format(s5))
print('====================DESAFIO 08====================')
m1 = float(input('Digite um valor em metros'))
v = m1 * 100
v1 = m1 * 1000
print('O valor em centimetros é {:.2f} e em milimetros é {:.2f}'.format(v,v1))
print('====================DESAFIO 09====================')
n5 = int(input('Digite um número inteiro para saber a sua tabuada'))
s6 = 1 * n5
s7 = 2 * n5
s8 = 3 * n5
s9 = 4 * n5
s10 = 5 * n5
s11 = 6 * n5
s12 = 7 * n5
s13 = 8 * n5
s14 = 9 * n5
s15 = 10 * n5
print('1 x {} = {}'.format(n5, s6))
print('2 x {} = {}'.format(n5, s7))
print('3 x {} = {}'.format(n5, s8))
print('4 x {} = {}'.format(n5, s9))
print('5 x {} = {}'.format(n5, s10))
print('6 x {} = {}'.format(n5, s11))
print('7 x {} = {}'.format(n5, s12))
print('8 x {} = {}'.format(n5, s13))
print('9 x {} = {}'.format(n5, s14))
print('10 x {} = {}'.format(n5, s15))
print('====================DESAFIO 10====================')
d = float(input('Digite quanto em $ você tem'))
d1 = d / 3.27
print('Você pode comprar {:.2f} dólares'.format(d1))
print('====================DESAFIO 11====================')
a = float(input('Digite a altura da sua parede'))
l = float(input('Digite a largura da sua parede'))
s16 = a * l
print('A sua parede mede {:.2f} metros quadrados'.format(s6))
a1 = float(input('Digite quantos metros quadrados a sua parede mede'))
s17 = s16 / 2
print('Para pintar a sua parede você precisa de exatamente {:.2f} litros de tinta'.format(s17))
print('====================DESAFIO 012====================')
p = float(input('Qual o preço do produto? R$'))
p1 = p - (p * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p,p1))
print('====================DESAFIO 0013====================')
s = float(input('Digite o seu salário'))
salario = s + (s * 15 / 100)
print('O seu salário que era R${:.2f}, com 15% de aumento vai ficar R${:.2f}'.format(s,salario))



