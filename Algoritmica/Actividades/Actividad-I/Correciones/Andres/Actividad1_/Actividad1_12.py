'''
En este programa creamos una lista con los primeros 1000 números y después accede uno a uno con el operador indexación
comprobando así que por muy alejado que estés del inicio o del final tarda siempre lo mismo.(con unas variacines mínimas dadas
por factores externos).
'''
import timeit
def prueba1():
    for i in l:
        p1 = l[i]
        return p1
    
l = []
for i in range(1000):
    l.append(i)

for j in l:
    t1 = timeit.Timer("prueba1()", "from __main__ import prueba1")
    print("Indexación ",t1.timeit(number=1000), "segundos")
