"""Escribe dos funciones para encontrar el número mínimo en una lista. La primera función debe comparar
cada número de una lista con todos los demás de la lista. 𝑶𝑶(𝒏𝒏 𝟐𝟐). La segunda función debe ser lineal 𝑶𝑶(𝒏𝒏).
12. Diseña un experimento para verificar que el operador indexación para listas es 𝑶𝑶(𝟏𝟏)
"""

import os as os


# Generamos una funcion que borre la pantalla
def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


borrar_pantalla()

import time
import random

#O(2)
def findMinnumb2(list):
    inicio = time.time()
    num = list[0]
    for i in range(len(list)):
        for j in range(len(list)):
            if num > list[j] and list[j] < list[i]:
                num = list[j]

    final = time.time()

    return num, final - inicio


L = [random.randint(0, 100000) for _ in range(400)]
numero2, tiempo2 = findMinnumb2(L)
print(
    f"La opcion de O(2) da como resultado resultado:{numero2} y ha tardado {round(tiempo2,5)} segundos"
)

#O(1)
def findMinnumb(list):
    inicio = time.time()
    num = list[0]
    for i in range(len(list)):
        if num > list[i]:
            num = list[i]

    final = time.time()
    return num, final - inicio


numero, tiempo = findMinnumb(L)
print(
    f"La opcion de O(1) da como resultado resultado:{numero} y ha tardado {round(tiempo,5)} segundos"
)
