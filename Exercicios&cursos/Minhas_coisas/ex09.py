from time import sleep
a = []
def lista(a = []):
    for c in range(0, 5):
        a.append(int(input(f'{c + 1}º Digite um número: ')))
    print(f'lista de números digitados: ', end=' ')
    for n in a:
        print(f'{n}', end='|')
lista()
sleep(2)
print('\nProximo...')
sleep(2)
lista()







