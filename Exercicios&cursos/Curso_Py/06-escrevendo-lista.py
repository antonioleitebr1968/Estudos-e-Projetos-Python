arquivo = open("arquivo_teste_dois.txt", "w")

linhas = ["A Centopeia – Marina Colasanti\n", "Quem foi que primeiro\n", "teve a ideia\n", "de contar um por um\n",
          "os pés da centopeia?\n", "Se uma pata você arranca\n", "será que a bichinha manca?\n",
          "E responda antes que eu esqueça\n", "se existe o bicho de cem pés\n", "será que existe algum de cem cabeças?\n"]

arquivo.writelines(linhas)
arquivo.close()