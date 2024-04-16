#Importamos librerías
import random
from timeit import Timer
from Busqueda_13_14 import* #Aquí están definidos todos los métodos de búsqueda

#Creamos la lista ordenada de números aleatorios:
def crear_lista(n):
    lista=[]
    for i in range(0,n,1):
        lista.append(random.randint(0,10000000))
    return lista

def ordenar_lista(lista):
    return sorted(lista)

#Benchmarks:
Secuencial_Optima=Timer("Busq_Secuencial_Opt(lista_ordenada,valor)","from __main__ import Busq_Secuencial_Opt,lista_ordenada,valor")
Secuencial_NoOptima=Timer("Busq_Secuencial_NoOpt(lista,valor)","from __main__ import Busq_Secuencial_NoOpt,lista,valor")
Binaria_Optima=Timer("Busq_Binaria_Opt(lista_ordenada,valor)","from __main__ import Busq_Binaria_Opt,lista_ordenada,valor")
Binaria_Rec_Optima=Timer("Busq_Binaria_Rec_Opt(lista_ordenada, valor,0,len(lista_ordenada)-1)","from __main__ import Busq_Binaria_Rec_Opt,lista_ordenada,valor")
Binaria_Rec_Optima_corte=Timer("Busq_Binaria_Rec_Opt_corte(lista_ordenada, valor)","from __main__ import Busq_Binaria_Rec_Opt_corte,lista_ordenada,valor")

#Inicializamos los valores de medias:
media1=0
media2=0
media3=0
media4=0
media5=0
contador=0

print("       \t ----Secuencial---- \t Binaria \t ---Binaria_Recursiva---")
print("Tamaño \t Optima    NoOptima \t Optima  \t  No Corte    Corte  ")

#Entramos en un bucle para hacer un benchmark de las funciones modificando el tamaño de la lista:
for j in range(0,30,1):
    lista=crear_lista(200)
    lista_ordenada=ordenar_lista(lista)
    valor=random.randint(0,10000000)

    #Empezamos los Benchmark:
    t1=Secuencial_Optima.timeit(number=1000)
    t2=Secuencial_NoOptima.timeit(number=1000)
    t3=Binaria_Optima.timeit(number=1000)
    t4=Binaria_Rec_Optima.timeit(number=1000)
    t5=Binaria_Rec_Optima_corte.timeit(number=1000)

    #Comunicamos resultados:
    print(f"200 \t {t1:.5f}   {t2:.5f} \t {t3:.5f} \t  {t4:.5f}     {t5:.5f}")

    #Calculamos las medias de cada método de búsqueda para comunicarla al final:
    media1+=t1
    media2+=t2
    media3+=t3
    media4+=t4
    media5+=t5
    contador+=1

#Comunicamos las medias:
media1/=contador
media2/=contador
media3/=contador
media4/=contador
media5/=contador

print()
print(f"media: \t {media1:.5f}   {media2:.5f} \t {t3:.5f} \t  {media4:.5f}     {media5:.5f}")
