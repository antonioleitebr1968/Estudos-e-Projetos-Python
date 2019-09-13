from pylab import *

#############VARIÁVEIS CONTENDO CORES##################
AZUL = '#48D1CC'
CINZA = '#A9A9A9'
ROXO = '#6A5ACD'
ROSA = '#FF69B4'
AZUL_CLARIN = '#00BFFF'
AZUL_CLARO_DA_PESTE = '#87CEFA'
VERMELHO = '#A52A2A'
VERDE_CLARO = '#00FF00'
SEI_LA = '#FFDEAD'
LARANJA = '#FF8C00'
AZUL_CINZA = '#B0C4DE'
PASTEL = '#E6E6FA'
#######################################################

names = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]

values = [2650, 3240, 3887, 3567, 5765, 4672, 9500, 3888, 12527, 10465, 11200,
          8773,]

#read_file = open("anual.csv")

"""for line in read_file:
    name, value = (line.strip().split(';'))
    names.append(name)
    values.append(float(value))"""

subplots_adjust(bottom=.16, right=0.97)

tick_params(axis='x', color=PASTEL)
tick_params(axis='y', color=AZUL_CINZA)
xlabel('Meses', color=VERMELHO)
ylabel('Faturamento', color=VERMELHO)
title('Faturamento anual da empresa', color=ROXO)


pos = arange(len(names)) + .5

bar(pos, values, align='center', color=ROXO)
xticks(pos, names, rotation=30, size='small')
grid(True)
show()