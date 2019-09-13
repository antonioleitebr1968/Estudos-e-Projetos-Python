from time import sleep
contc = 0# para respostas certas
conte = 0# para respostas erradas
reps = 'X'# definição de reposta
avançar = 'Próxima pergunta...'
faixa1 = '-=' * 50
faixa2 = '-' * 100
titulo = 'BEM VINDO AO MEU QUIZ!'
titulo2 = 'OBS: Quiz com conhecimento variado, Boa sorte!'
def proximo():
    print(faixa2)
    print(f'\033[1;31m{avançar:^100}\033[m')
    sleep(1)
    print(faixa2)
print(faixa1)
print(f'{titulo:^100}')
print(f'{titulo2:^100}')
print(faixa1)
print('Você precisa obter no mínimo tantos pontos para ter exito!')
print(faixa2)
while reps not in 'SN':
    reps = str(input('Quer começar? [S/N] ')).upper().strip()[0]
    if reps == 'N':
        break
    if reps == 'S':
        print('Muito bem, vamos começar!')
        print('PROCESSANDO...')
        sleep(1)
        resp1 = str(input('1º) Qual a capital do RN? ')).strip().upper()
        if resp1 == 'NATAL':
            print('Resposta correta!')
            contc += 100
        else:
            print('Resposta errada!')
            conte += 10
        proximo()
        print('2º) Digite a opção correta:')
        print('Quanto é 999 + 3 x 600 - 900 % 2 ?')
        print('''Suas opções 
[ 1 ] 2349
[ 2 ] 2140
[ 3 ] 1150
[ 4 ] 42
[ 5 ] 2050''')
        resp2 = int(input('Digite a sua opção aqui >>> '))
        if resp2 == 1:
            print('resposta correta!')
            contc += 100
        elif resp2 != 1:
            print('resposta errada')
            conte += 10
        proximo()
        resp3 = str(input('3º) Baseando-se no Anime "Dragon Ball Super" qual o nome do vilão que auto se titula um Deus? ')).strip().upper()
        if resp3 == 'GOKU BLACK':
            print('Resposta correta!')
            contc += 100
        if resp3 != 'GOKU BLACK':
            print('resposta errada!')
            conte += 10
        proximo()
        print('''4º) Digite a opção correta! Qual a média de idade de um grupo em que há 6 pessoas de 14 anos, 9 pessoas de 20 anos
e 5 pessoas de 16 anos?''')
        print('''Suas opções: 
[ 1 ] 18.1 anos
[ 2 ] 17.0 anos
[ 3 ] 15.7 anos
[ 4 ] 19.4 anos
[ 5 ] 17.2 anos''')
        resp4 = int(input('Digite a sua opção aqui >>> '))
        if resp4 == 5:
            print('reposta correta!')
            contc += 100
        else:
            print('resposta errada!')
            conte += 10
        proximo()
        resp5 = str(input('5º) Qual o time que foi mais vezes campeão da "Liga dos campeões da UEFA" ?? ')).upper().strip()
        if resp5 == 'REAL MADRID':
            print('resposta correta!')
            contc += 100
        else:
            print('resposta errada!')
            conte += 10
        proximo()
        resp6 = str(input('6º) A palavra "amor" esta dentro de qual palavra? \nDica: É uma data amorosa que geralmente casais comemoram. ')).strip().upper()[1:5]
        if resp6 == 'AMOR':
            print('reposta correta!')
            contc += 100
        else:
            print('resposta errada!')
            conte += 10
        proximo()
        resp7 = str(input('7º) Qual a seleção mais vezes campeã mundial? ')).upper().strip()
        if resp7 == 'BRASIL':
            print('resposta correta!')
            contc += 100
        else:
            print('resposta errada!')
            conte += 10
        proximo()
        resp8 = str(input('8º) O hamster possui 4 dedos nas patas dianteiras e 5 nas traseiras. \nIsso é verdade? ')).upper().strip()
        if resp8 == 'S':
            print('Resposta correta!')
            contc += 100
        else:
            print('Resposta errada!')
            conte += 10


print(f'Sua média de acertos foi de tantos')
# continua depois...