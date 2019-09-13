faixa = '-=' * 30
faixa2 = '-' * 60
titulo = 'ANALISE DE DADOS'
mulhermenor20 = homens = maior18 = 0
print(f'{faixa}')
print(f'{titulo:^60}')
print(f'{faixa}')
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = 'X'
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulhermenor20 += 1
    resposta = 'X'
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
    print(f'{faixa2}')
print(faixa)
print('FIM DO PROGRAMA')
print(faixa)
print(f'No total foram {maior18} pessoas maiores de 18 anos,', end=' ')
print(f' {homens} homens registrados e {mulhermenor20} mulheres menores de 20 anos.')
