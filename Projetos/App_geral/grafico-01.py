import matplotlib.pyplot as plt

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
x = [500, 420, 320, 412]
y = [100, 1000, 20, 877]

fig = plt.figure()
rect = fig.patch
rect.set_facecolor(ROXO)


ax1 = fig.add_subplot(1, 1, 1, axisbg=PASTEL)
ax1.plot(x, y, 'r',linewidth=3.3, linestyle='--')
ax1.set_title('Matplotlib exemplo')
ax1.set_xlabel('xlabel')
ax1.set_ylabel('ylabel')

"""plt.plot([500, 420, 320, 412], [100, 1000, 20, 877])

plt.title("Empresa X")
plt.xlabel('x label')
plt.ylabel('y label')"""

plt.show()
