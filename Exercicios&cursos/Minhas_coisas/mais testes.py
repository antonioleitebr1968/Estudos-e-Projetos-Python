a = b = 'x'
def soma_max(a, b):
    a = int(input('Valor de (a)? '))
    b = int(input('Valor de (b)? '))
    if a > b:
        print(a, 'Maior que ', b)
    elif a == b:
        print(a, 'E', b, 'tem o mesmo valor!')
    else:
        print(b, 'Maior que', a)

nome = str(input('Qual seu nome? ')).strip().capitalize()
n = nome.split()
print(f'Ok {n[0]} vou chamar a função soma_max !')
soma_max(a, b)
#primeira função com o "def

