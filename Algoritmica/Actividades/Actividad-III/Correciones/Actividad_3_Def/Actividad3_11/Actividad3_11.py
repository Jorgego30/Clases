#Importamos librerías
import random
from timeit import Timer
from Ordenamiento_11 import* #Aquí están definidos todos los métodos de búsqueda

#Creamos la lista ordenada de números aleatorios:
def crear_lista(n):
    lista=[]
    for i in range(0,n,1):
        lista.append(random.randint(0,100000))
    return sorted(lista)

#Benchmarks:
Primero=Timer("Quicksort_primero(lista,0,len(lista)-1)","from __main__ import Quicksort_primero,lista")
Segundo=Timer("Quicksort_ultimo(lista,0,len(lista)-1)","from __main__ import Quicksort_ultimo,lista")
Tercero=Timer("Quicksort_aleatorio(lista,0,len(lista)-1)","from __main__ import Quicksort_aleatorio,lista")
Cuarto=Timer("Quicksort_mediana(lista,0,len(lista)-1)","from __main__ import Quicksort_mediana,lista")

#Inicializamos los valores de medias:
media1=0
media2=0
media3=0
media4=0
contador=0

print("       \t ------------------Quicksort con pivote------------------")
print("Tamaño \t Primero \t Ultimo \t Aleatorio \t Mediana  ")

#Entramos en un bucle para hacer un benchmark de las funciones modificando el tamaño de la lista:
for j in range(100,501,50):
    lista=crear_lista(j)

    #Empezamos los Benchmark:
    t1=Primero.timeit(number=1000)
    t2=Segundo.timeit(number=1000)
    t3=Tercero.timeit(number=1000)
    t4=Cuarto.timeit(number=1000)

    #Comunicamos resultados:
    print(f"{j} \t {t1:.5f} \t {t2:.5f} \t {t3:.5f} \t {t4:.5f}")

    #Calculamos las medias de cada método de búsqueda para comunicarla al final:
    media1+=t1
    media2+=t2
    media3+=t3
    media4+=t4
    contador+=1

#Comunicamos las medias:
media1/=contador
media2/=contador
media3/=contador
media4/=contador

print()
print(f"media \t {media1:.5f} \t {media2:.5f} \t {media3:.5f} \t {media4:.5f} ")

