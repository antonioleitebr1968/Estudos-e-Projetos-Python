lista_simples_inteiro = [1, 2, 8, 4, 5, 14]

meu_iter = iter(lista_simples_inteiro)


while True:
    try:
        elemento = next(meu_iter)
        print(elemento)
    except StopIteration:
        break


#print(next(meu_iter))
#print(next(meu_iter))
#print(next(meu_iter))
#print(next(meu_iter))
#print(next(meu_iter))
#print(next(meu_iter))
#print(next(meu_iter))
