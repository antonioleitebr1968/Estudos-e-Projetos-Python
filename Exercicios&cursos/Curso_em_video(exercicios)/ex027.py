n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer {}!'.format(nome[0]))
print('Seu primeiro nome é {}'.format(nome[0]), end=' ')
print('e o seu últiumo nome é {}'.format(nome[len(nome)-1]))



