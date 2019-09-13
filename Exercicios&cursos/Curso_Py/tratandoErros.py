#Exemplo um

valor = input("Informe um número: ")
try:
    soma = int(valor) + 10
    resultado = soma / int(valor)
except ZeroDivisionError:
    print("Ocorreu um erro de divisão por zero!")
except ValueError:
    print("Opa ocorreu um erro de valor!")

finally:
    print("Isso sempre é executado!")

print("\033[1;33;44mOcorrendo\033[m erro ou não, sou executado!")