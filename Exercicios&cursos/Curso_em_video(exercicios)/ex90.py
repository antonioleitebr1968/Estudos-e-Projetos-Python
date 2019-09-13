dic = {}
dic['nome'] = str(input('Nome: ')).strip().capitalize()
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
print(f'Média é igual a {dic["média"]}')
if dic['média'] >=7:
    dic['situação'] = 'Aprovado'
elif dic['média'] < 7:
    dic['situação'] = 'Reprovado'
print(f'Situação é igual a {dic["situação"]}')
