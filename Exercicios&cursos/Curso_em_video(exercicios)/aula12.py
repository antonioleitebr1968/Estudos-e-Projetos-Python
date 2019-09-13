#Estrutura condicional aninhada
nome = str(input('Qaul é seu nome? ')).strip().capitalize()
if nome == 'Matheus':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome =='Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica juliana':#O in verifica se tem um dos nomes dentro da string.
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

