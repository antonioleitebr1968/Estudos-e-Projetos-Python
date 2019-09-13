total = preçomaior = preçomenor = cont = 0
barato = 'X'
faixa = '-' * 50
faixa2 = '-=' * 25
finalizar = 'PROCESSO FINALIZAADO'
titulo = 'LOJA DO BARATO TEM ATÉ BRILHO PRA GATO'
print(faixa2)
print(f'{titulo:^50}')
print(faixa2)
while True:
    nome = str(input('Qual o nome do produto? ')).strip().upper()
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        preçomaior += 1
    if cont == 1 or preço < preçomenor:
        preçomenor = preço
        barato = nome
    pergunta = 'X'
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergunta == 'N':
        break
print(faixa)
print(f'{finalizar:^50}')
print(f'O total gasto foi de R${total:.2f}')
print(f'e {preçomaior} produtos que custaram mais de R$1000')
print(f'O nome do produto mais barato é {barato} e custa R${preçomenor:.2f}')
print(faixa)
