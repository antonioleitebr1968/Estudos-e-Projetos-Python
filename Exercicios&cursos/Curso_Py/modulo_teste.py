def converte_inteiro(string):
    if string not in ("0", "1", "2", "3", "4", "5", "6", "7",
                      "8", "9"):
        raise ValueError("Informe um número de 0 a 9!")
    return int(string)
