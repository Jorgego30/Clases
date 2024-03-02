import timeit
import random


print("%10s %10s   %10s" % ("tamaño", "lista", "diccionario"))
for i in range(10000, 1000001, 20000):

    x = list(range(1000000))
    t_lista = timeit.Timer("del x[random.randrange(%d)]" % i, "from __main__ import random, x")
    tiempo_lista = t_lista.timeit(number=100)
    
    y = {j: random.random() for j in range(i)}
    t_diccionario = timeit.Timer("del y[random.randrange(%d)]" % i, "from __main__ import random, y")
    tiempo_diccionario = t_diccionario.timeit(number=100)

    print("%10d %10.3f %10.3f" % (i, tiempo_lista, tiempo_diccionario))
