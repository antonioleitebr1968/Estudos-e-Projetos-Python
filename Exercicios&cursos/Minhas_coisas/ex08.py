### EXERCÍCIO 19 ###
#Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
# O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
faixa = '-=' * 50
faixa2 = '-' * 100
titulo = 'Qual o melhor Sistema Operacional para uso em servidores?'
system = 'Sistema operacional'
votos = 'votos'
vencedor = 'VENCEDOR'
escolha1 = escolha2 = escolha3 = escolha4 = escolha5 = escolha6 = 0
soma = 0
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
print(f'\033[1;30m {faixa}\033[m')
print('  ')
print(f'\033[1;36m{titulo:^100}\033[m')
print('   ')
print(f'\033[1;30m{faixa}\033[m')
print('   ')
while True:
    pos = 0
    print('\033[1;36mAs possíveis respostas são: ')
    print('   ')
    print('''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outros''')
    print('Digite "0" para encerrar o programa.')
    print('   ')
    opção = int(input('Digite a sua opção aqui >>> '))
    print('   ')
    if opção == 0:
        break
    if opção == 1:
        escolha1 = int(input('Você escolheu Windows Server. Digite aqui a quantidade de votos >>> '))
        soma += escolha1
        lista1.append(escolha1)
    if opção == 2:
        escolha2 = int(input('Você escolheu Unix. Digite aqui a quantidade de votos >>> '))
        soma += escolha2
        lista2.append(escolha2)
    if opção == 3:
        escolha3 = int(input('Você escolheu Linux. Digite aqui a quantidade de votos >>> '))
        soma += escolha3
        lista3.append(escolha3)
    if opção == 4:
        escolha4 = int(input('Você escolheu Netware. Digite aqui a quantidade de votos >>> '))
        soma += escolha4
        lista4.append(escolha4)
    if opção == 5:
        escolha5 = int(input('Você escolheu Mac OS. Digite aqui a quantidade de votos >>> '))
        soma += escolha5
        lista5.append(escolha5)
    if opção == 6:
        escolha6 = int(input('Você escolheu a opção Outros. Digite aqui a quantidade de votos >>> '))
        soma += escolha6
        lista6.append(escolha6)
    if opção > 6 or opção < 0:
        print('Opção invalida. Tente novamente...')
    pos += 1
    print(f'\033[1;30m{faixa2}\033[m')
WindowsServer = escolha1 * 100 / soma#representa um valor retirado de um montante em porcentagem///Teoricamente forma errada mas funciona
Unix = escolha2 * 100 / soma
Linux = escolha3 * 100 / soma
Netware = escolha4 * 100 / soma
MacOS = escolha5 * 100 / soma
Outros = escolha6 * 100 / soma
'''WindowsServer = escolha1 * soma / 100#representa um valor retirado de um montante em porcentagem///Teoricamente é a forma correta !
Unix = escolha2 * soma / 100
Linux = escolha3 * soma / 100
Netware = escolha4 * soma / 100
MacOS = escolha5 * soma / 100
Outros = escolha6 * soma / 100'''
print(f'\033[1;30m{faixa2}\033[m')
print(f'\033[1;36m{system:^100}')
print('   ')
print(f'Windows Server obteve {escolha1} votos que correspondem a {WindowsServer:.2f}% do total de {soma} votos. ')
print('   ')
print(f'Unix obteve {escolha2} votos que correspondem a {Unix:.2f}% do total de {soma} votos. ')
print('   ')
print(f'Linux obteve {escolha3} votos que correspondem a {Linux:.2f}% do total de {soma} votos.')
print('   ')
print(f'Netware obteve {escolha4} votos que correspondem a {Netware:.2f}% do total de {soma} votos.')
print('   ')
print(f'Mac Os obteve {escolha5} votos que correspondem a {MacOS:.2f}% do total de {soma} votos.')
print('   ')
print(f'Outros obtiveram {escolha6} votos que correspondem a {Outros:.2f}% do total de {soma} votos.')
print(f'\033[1;30m{faixa2}\033[m')
print(f'\033[1;36m{vencedor:^100}')
listafinal = lista1 + lista2 + lista3 + lista4 + lista5 + lista6
if max(listafinal) == escolha1:
    print('A categoria mais votada foi \033[1;31mWindows Server.\033[m')
if max(listafinal) == escolha2:
    print('A categoria mais votada foi \033[1;31mUnix\033[m')
if max(listafinal) == escolha3:
    print('A categoria mais votada foi \033[1;31mLinux\033[m')
if max(listafinal) == escolha4:
    print('A categoria mais votada foi \033[1;31mNetware\033[m')
if max(listafinal) == escolha5:
    print('A categoria mais votada foi \033[1;31mMac OS\033[m')
if max(listafinal) == escolha6:
    print('A categoria mais votada foi \033[1;31mOutros\033[m')
final = 'FINISH !!!'
print(f'\033[1;33m{final:^100}\033[m')
