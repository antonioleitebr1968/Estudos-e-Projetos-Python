while True:
    print('-' * 50)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 50)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('PROGRAMA ENCERRADO. Volte sempre!')

