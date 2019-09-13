#Exemplo um

valor = input("Informe um número: ")
try:
    soma = int(valor) + 10
    resultado = soma / int(valor)
except ZeroDivisionError as erro:
    print("Ocorreu um erro de divisão por zero! Erro:", erro)
except ValueError as e:
    print("Opa ocorreu um erro de valor! Erro:", e)

finally:
    print("Isso sempre é executado!")