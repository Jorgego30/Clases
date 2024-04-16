'''Actividad 12:

Genera una pequeña lista aleatoria de números enteros. Muestra paso a paso cómo es ordenada dicha lista
por los siguientes algoritmos:
ordenamiento burbuja, en todas sus variantes
ordenamiento por selección
ordenamiento por inserción
ordenamiento de Shell (con distintos valores de los incrementos)
ordenamiento por mezcla
ordenamiento rápido (decide sobre el valor pivote)
'''

import random

# Generar una lista aleatoria de 10 números enteros entre 0 y 100
lista = [random.randint(0, 100) for _ in range(10)]

# Mostrar la lista original
print("Lista original:", lista)


def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print("Paso:", lista)
print("Ordenaimento burbuja: ")
ordenamiento_burbuja(lista.copy())

def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        print("Paso:", lista)
print("Ordenamiento selección: ")
ordenamiento_seleccion(lista.copy())

def ordenamiento_insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
        print("Paso:", lista)
print("Ordenamiento inserción: ")
ordenamiento_insercion(lista.copy())

def ordenamiento_shell(lista):
    n = len(lista)
    brecha = n // 2
    while brecha > 0:
        for i in range(brecha, n):
            temp = lista[i]
            j = i
            while j >= brecha and lista[j - brecha] > temp:
                lista[j] = lista[j - brecha]
                j -= brecha
            lista[j] = temp
        brecha //= 2
        print("Paso:", lista)
print("Ordenamiento shell: ")
ordenamiento_shell(lista.copy())

def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print("Paso:", lista)
print("Ordenamiento Mezcla: ")
ordenamiento_mezcla(lista.copy())

def ordenamiento_rapido(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return ordenamiento_rapido(menores) + [pivote] + ordenamiento_rapido(mayores)
print("Ordenamiento rápido: ")
print("Lista ordenada:", ordenamiento_rapido(lista.copy()))
