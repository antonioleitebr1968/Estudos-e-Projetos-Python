from time import sleep
chamaEu = lambda: print('Uhuuuuuuuuuuu')
def setInterval(func):
    while True:
        sleep(0.5)
        func()
        print('chamei a função\n\n')
setInterval(chamaEu)
