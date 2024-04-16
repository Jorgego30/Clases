'''
Ejercicio 19.
Utilizando un generador de números aleatorios, crea una lista de 500 enteros. Realiza una prueba de
referencia usando al menos 3 de los algoritmos de ordenamiento de los apuntes. ¿Cuál es la diferencia en la
velocidad de ejecución? ¿Cuáles son tus conclusiones?'''

from random import randint
import time
import os
import statistics
os.system('clear')

#Generamos una lista aleatoria
def generar_lista_aleatoria():
    lista_aleatoria=[]
    for i in range(500):
        lista_aleatoria.append(randint(0,1000))

    return lista_aleatoria

#Realizamos el ordenamiento burbuja
def ordenamientoBurbuja(unaLista,j):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
    
        j+=1

#Realizamos el ordenamiento rápido
def ordenamientoRapido(unaLista):
    ordenamientoRapidoAuxiliar(unaLista, 0, len(unaLista)-1)


def ordenamientoRapidoAuxiliar(unaLista, primero, ultimo):
    if primero < ultimo:

        puntoDivision = particion(unaLista, primero, ultimo)

        ordenamientoRapidoAuxiliar(unaLista, primero, puntoDivision-1)
        ordenamientoRapidoAuxiliar(unaLista, puntoDivision+1, ultimo)


def particion(unaLista, primero, ultimo):
    valorPivote = unaLista[primero]

    marcaIzq = primero+1
    marcaDer = ultimo

    hecho = False
    while not hecho:

        while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1

        while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer - 1

        if marcaDer < marcaIzq:
            hecho = True
        else:
            unaLista[marcaIzq],unaLista[marcaDer] = unaLista[marcaDer],unaLista[marcaIzq]

    unaLista[primero],unaLista[marcaDer] = unaLista[marcaDer],unaLista[primero]

    return marcaDer

#Realizamos el ordenamiento por inserción
def ordenamientoPorInsercion(unaLista,i):
    for indice in range(1, len(unaLista)):

        valorActual = unaLista[indice]
        posicion = indice

        while posicion > 0 and unaLista[posicion-1] > valorActual:
            unaLista[posicion] = unaLista[posicion-1]
            posicion = posicion-1

        unaLista[posicion] = valorActual
        
        i+=1

#Realizamos el main llamando a las funciones de forma ordenada
def main():
    print('\n\t***Realizaremos un Benchmark 50 veces distintas, presentando las medias, con distintas funciones***')

    unaLista = generar_lista_aleatoria()
    unaLista2 = unaLista
    unaLista3 = unaLista
    unaLista4 = unaLista
    unaLista5 = unaLista

    ordenamientoBurbuja_lista=[]
    sorted_lista=[]
    ordenamientoPorInsercion_lista=[]
    ordenamientoBurbuja_lista=[]

    #Realizamos una media de 50 veces para presentar un benchmark más exacto
    for i in range(50):
        start=time.time()
        ordenamientoRapido(unaLista)
        end=time.time()
        ordenamientoBurbuja_lista.append(end-start)

        start=time.time()
        sorted(unaLista2)
        end=time.time()
        sorted_lista.append(end-start)

        i=0
        start=time.time()
        ordenamientoPorInsercion(unaLista3,i)
        end=time.time()
        ordenamientoPorInsercion_lista.append(end-start)

        i=0
        start=time.time()
        ordenamientoBurbuja(unaLista4,i)
        end=time.time()
        ordenamientoBurbuja_lista.append(end-start)

    #Pintamos el resultado de las funciones, junto a la función de python, sorted.
    print('\n\tEl ordenamiento rápido tarda con esta lista de 500 números: ', statistics.mean(ordenamientoBurbuja_lista))
    print('\tCon la función de python, sorted, tarda con esta lista de 500 números: ', statistics.mean(sorted_lista))
    print('\tEl ordenamiento por inserción tarda con esta lista de 500 números: ', statistics.mean(ordenamientoPorInsercion_lista))
    print('\tEl ordenamiento burbuja tarda con esta lista de 500 números: ', statistics.mean(ordenamientoBurbuja_lista))

main()