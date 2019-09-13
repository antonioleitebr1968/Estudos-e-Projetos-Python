brasileirão = ('Flamengo', 'Atlético-MG', 'São Paulo',
               'Internacional', 'Grêmio', 'Palmeiras',
               'Sport', 'Cruzeiro', 'Botafogo', 'Corinthians',
               'Vasco', 'Fluminense', 'América-MG', 'Chapecoense',
               'Santos', 'Vitória-BA', 'Bahia', 'Paraná', 'Atlético-PR',
               'Ceará')
faixa = '=' * 280
print(faixa)
print(f'Lista de times do Brasileirão: {brasileirão}')
print(faixa)
print(f'Os 5 primeiros colocados são {brasileirão[0:5]}')
print(faixa)
print(f'Os 4 últimos são {brasileirão[-4:]}')
print(faixa)
print(f'Times na ordem aldabética: {sorted(brasileirão)}')
print(faixa)
print(f'A Chapecoense está na {brasileirão.index("Chapecoense")+ 1}ª posição')#coloquei aspas duplas pq não da pra colocar as simples dentro de aspas simples na mesma string
print(faixa)
