númeração = ('Zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Ôito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
             'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num <= 0 or num <= 20:#maneira simplificada: if 0 <= num <=20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {númeração[num]}')