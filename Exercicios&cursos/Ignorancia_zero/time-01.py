import time
"""print(time.asctime())#mostra o dia da semana, o mês, o dia do mês, a hora exata e o ano
a = time.localtime()
print(a[0])#ano
print(a[1])#mês
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])#horario de verão
print(a[8])#nº do dia no ano
print(a.tm_zone)#país
print(a.tm_gmtoff)"""

"""print(time.time())#todos os segundos desde a epoca
t0 = time.time()
tf = time.time()
dt = tf - t0
print(t0)
print(tf)"""

"""print(time.process_time())#tempo de processamento da linha do script
print(time.localtime(time.time()))
print(time.localtime(1))
a = time.localtime()
print(a.tm_zone)

print(time.gmtime())
print(time.gmtime(1))

print(time.asctime(time.localtime(time.time())))"""


########################################
#printando 'eu te amo por 5 segundos
marcador = time.time()
print(marcador)
while True:
    print('I love u')
    tempo = time.time()
    if tempo - marcador > 5:
        break
########################################"""
