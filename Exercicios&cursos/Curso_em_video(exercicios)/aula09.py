frase = 'Curso em Vídeo Python'
print('='*40, 'Bem vindo aos exemplos da Aula 09', '='*40)
print(' '*50, 'Manipulando texto :)', ' '*50)
print('')
print('='*51, 'Fatiamento', '='*52)
print('')
print('1>>', frase[9])#ele vai indentificar a caractere 9 ou seja a 10 pq para o python começa a contar da caractere 0
print('')
print('2>>', frase[9:13])#ele vai pegar do caractere 9 até o 13
print('')
print('3>>', frase[9:21])#ele vai fatiar do 9 ate o final pq a caractere 21 n existe
print('')
print('4>>', frase[9:21:2])#ele vai fatiar do 9 até 21 pulando de dois em dois caracteres
print('')
print('5>>', frase[:5])#ele vai começar do inicio até o caractere 5
print('')
print('6>>', frase[15:])#ele vai começar do 15 até o final da string
print('')
print('7>>', frase[9::3])#ele vai começar no 9 e vai até o final pulando de 3 em 3
print('')
print('='*53, 'Análise', '='*53)
print('8>>', len(frase))#mostra quantas caracteres tem na frase
print('')
print('9>>', frase.count('o', 0, 13))#fatia e mostra quantas caracteres 'o' tem na frase do 0 ao 13
print('')
print('10>>', frase.find('deo'))#ele vai me dizer em que momento começou o 'deo'
print('')
print('11>>', frase.find('Android'))#ele vai mostrar -1 significa que a string que vc tentou encontrar não existe.
print('')
print('12>>', 'Curso' in frase)#ele vai me dizer se dentro da frase existe a palavra 'Curso' usando True ou False.
print('')
print('='*50, 'Transformação', '='*50)
print('')
print('13>>', frase.replace('Python', 'Android'))#ele substitui a palavra 'Python por a 'Android'
print('')
print('14>>', frase.upper())#ele vai manter as maiúsculas e transformar todas as que não são em maiúsculas
print('')
print('15>>', frase.lower())#mantem o que é minúscula e transforma o restante em minúscula
print('')
print('16>>', frase.capitalize())#transforma toda a string em minúscula deixando apenas a primeira caractere em maiúscula
print('')
print('17>>', frase.title())#ele vai analisar quantas palavras tem na string utilizando o espaço entre cada palavra
print('')
print('18>>', frase.strip())#ele vai remover todos os espaços inúteis no final e no inicio da string, mantendo a penas os do meio.
print('')
print('19>>', frase.rstrip())#remove todos os espaços a direita
print('')
print('20>>', frase.lstrip())#remove todos os espaços da esquerda
print('')
print('='*52, 'Divisão', '='*54)
print('')
print('21>>', frase.split())#Divide uma string em uma lista de strings númeradas
print('')
print('22>>', '-'.join(frase))#se eu tenho uma string dividida em uma lista essa função junta a lista e usa o separador'-' entre os espaços
print('')
print('='*53, 'FINISH', '='*54)


