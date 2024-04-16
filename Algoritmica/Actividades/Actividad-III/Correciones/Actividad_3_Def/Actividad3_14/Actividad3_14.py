#Importamos librerías
import random
from timeit import Timer
from Busqueda_13_14 import* #Aquí están definidos todos los métodos de búsqueda

#Creamos la lista ordenada de números aleatorios:
def crear_lista(n):
    lista=[]
    for i in range(0,n,1):
        lista.append(random.randint(0,10000000))
    return sorted(lista)

#Benchmarks:
Binaria_Optima=Timer("Busq_Binaria_Opt(lista,valor)","from __main__ import Busq_Binaria_Opt,lista,valor")
Binaria_Rec_Optima=Timer("Busq_Binaria_Rec_Opt(lista, valor,0,len(lista)-1)","from __main__ import Busq_Binaria_Rec_Opt,lista,valor")
Binaria_Rec_Optima_corte=Timer("Busq_Binaria_Rec_Opt_corte(lista, valor)","from __main__ import Busq_Binaria_Rec_Opt_corte,lista,valor")

#Inicializamos los valores de medias:
media1=0
media2=0
media3=0
contador=0

print("       \t Binaria \t --Binaria_Recursiva--")
print("Tamaño \t Optima  \t   Corte    No Corte ")

#Entramos en un bucle para hacer un benchmark de las funciones modificando el tamaño de la lista:
for j in range(1000,10001,500):
    lista=crear_lista(j)
    valor=random.randint(0,10000000)

    #Empezamos los Benchmark:
    t1=Binaria_Optima.timeit(number=1000)
    t3=Binaria_Rec_Optima.timeit(number=1000)
    t2=Binaria_Rec_Optima_corte.timeit(number=1000)

    #Comunicamos resultados:
    print(f"{j} \t {t1:.5f} \t  {t2:.5f}    {t3:.5f}")

    #Calculamos las medias de cada método de búsqueda para comunicarla al final:
    media1+=t1
    media2+=t2
    media3+=t3
    contador+=1

#Comunicamos las medias:
media1/=contador
media2/=contador
media3/=contador

print()
print(f"media: \t {media1:.5f} \t  {media2:.5f}    {media3:.5f} ")

print()
print("De estos resultados podemos observar que el método de búsqueda binaria es mejor cuando no se hace de forma recursiva y que el peor método es el que usa el operador corte ya que este consume tiempo de por si solo")
