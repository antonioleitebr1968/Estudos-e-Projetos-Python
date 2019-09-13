#EXERCICIO 17
#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
# os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
faixa = '-=' * 30
faixa2 = '-' * 60
titulo = 'REGISTRO DE DADOS PARA ATLETAS'
titulo2 = 'Categoria salto'
final = 'FINISH'
print(faixa)
print(f'{titulo:^60}')
print(f'{titulo2:^60}')
print(faixa)
print('Obs: não informe o nome para finalizar o programa')
print(faixa2)
soma = 0
while True:
    lista = []# lista
    nom1 = str(input('Nome do atleta: ')).strip().upper()
    if nom1 == '':
        break
    for c in range(0, 5):
        salto = float(input(f'{c + 1}º salto: '))
        soma += salto
        média = soma / 5
        lista.append(salto)
    print(faixa2)
    print('Resultado final do atleta')
    print(f'Atleta: {nom1}')
    print('Saltos: ', end='')
    for s in lista:
        print(s, end=' | ')
    #print(f'Saltos: {lista[1:]}')
    print(f'\nMédia de saltos: {média:.2f}')
    print(faixa2)
print(faixa2)
print(f'{final:^60}')
print(faixa2)
