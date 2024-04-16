#Importamos librerías:
import random

#Ordena la lista cuando el pivote es el primer elemento
def Particion1(lista, izq, der, pivote):
    i = izq + 1
    j = der
    
    while True:
        while i <= j and lista[i] <= pivote:
            i += 1
        while i <= j and lista[j] >= pivote:
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
        else:
            break
    
    lista[izq], lista[j] = lista[j], lista[izq]
    return j

def Quicksort_primero(lista, izq, der):
    if izq < der:
        #Se busca el pivote tal que los números que quedan a la izquierda de este son menor y a la derecha mayor
        pi = Particion1(lista, izq, der,lista[izq])

        #Llamadas recursivas a la función
        Quicksort_primero(lista, izq, pi - 1)
        Quicksort_primero(lista, pi + 1, der)

#Ordena la lista cuando el pivote es el último elemento
def Particion2(lista, izq, der, pivote):
    i = izq - 1
    
    for j in range(izq, der):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[der] = lista[der], lista[i + 1]
    return i + 1

def Quicksort_ultimo(lista, izq, der):
    if izq < der:
        #Se busca el pivote tal que los números que quedan a la izquierda de este son menor y a la derecha mayor
        pi = Particion2(lista, izq, der,lista[der])

        #Llamadas recursivas a la función
        Quicksort_ultimo(lista, izq, pi - 1)
        Quicksort_ultimo(lista, pi + 1, der)

#Ordena la lista cuando el pivote es un elemento aleatorio
def Particion3(lista, izq, der,pivote,pos_pivote):
    lista[pos_pivote], lista[der] = lista[der], lista[pos_pivote]  #Coloca el pivote en el último lugar
    i = izq - 1
    
    for j in range(izq, der):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[der] = lista[der], lista[i + 1]
    return i + 1

def Quicksort_aleatorio(lista, izq, der):
    if izq < der:
        pos_pivote=random.randint(izq,der)
        #Se busca el pivote tal que los números que quedan a la izquierda de este son menor y a la derecha mayor
        pi = Particion3(lista, izq, der,lista[pos_pivote],pos_pivote)

        #Llamadas recursivas a la función
        Quicksort_aleatorio(lista, izq, pi - 1)
        Quicksort_aleatorio(lista, pi + 1, der)

#Ordena la lista cuando el pivote es la mediana
def Particion4(lista, izq, der,pivote):
    i = izq - 1
    
    for j in range(izq, der):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[der] = lista[der], lista[i + 1]
    return i + 1

def median_of_three(lista, izq, der):
    mediana = (izq + der) // 2
    #Encuentra la mediana entre el primer, medio y último elemento
    if lista[izq] < lista[mediana]:
        if lista[mediana] < lista[der]:
            return mediana
        elif lista[izq] < lista[der]:
            return der
        else:
            return izq
    else:
        if lista[izq] < lista[der]:
            return izq
        elif lista[mediana] < lista[der]:
            return der
        else:
            return mediana

def Quicksort_mediana(lista, izq, der):
    if izq < der:
        #Calculamos el pivote:
        pivot_index=median_of_three(lista, izq, der)
        lista[pivot_index], lista[der] = lista[der], lista[pivot_index]  #Coloca el pivote en el último lugar

        #Se busca el pivote tal que los números que quedan a la izquierda de este son menor y a la derecha mayor
        pi = Particion4(lista, izq, der,lista[der])

        #Llamadas recursivas a la función
        Quicksort_mediana(lista, izq, pi - 1)
        Quicksort_mediana(lista, pi + 1, der)

