resposta = 'S'
soma = quant = média = maior = menor = 0
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / quant
print('Você digitou {} números, e a média foi de {}'.format(quant, média))
print('O maior foi {} e o menor é {}'.format(maior, menor))
print('PROGRAMA FINALIZADO')