"""Diseña un experimento para verificar que las operaciones de obtención y asignación de ítems para
diccionarios son 𝑶(𝟏)"""

import timeit
import random
import os as os


# Generamos una funcion que borre la pantalla
def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


borrar_pantalla()


# Esta funcion nos devuelce el tiempo que se tarda en obtner un elemento concreto de un diccionario introducido
def obtener_tiempo_obtencion(diccionario, clave):
    return timeit.timeit(lambda: diccionario[clave], number=1000)


# Esta funcion nos devuelce el tiempo que se tarda en asignar un elemento a una clave de un diccionario introducido
def obtener_tiempo_asignacion(diccionario, clave, Valor):
    return timeit.timeit(lambda: diccionario.update({clave: Valor}), number=1000)


# Esta funcion genera diccionarios de elementos aleatorios con una longitud determinada introducida
def generar_diccionarios(tamaños_diccionario):
    tiempos_obtencion = []
    tiempos_asignacion = []
    # Con esto ademas de generar los diccionarios obtenemos el tiempo que se tarda en cambiar un elemento y random
    for i in tamaños_diccionario:
        diccionario = {j: random.random() for j in range(i)}
        clave = random.randint(
            0, i - 1
        )  # generamos una clave random que este dentro del rango de el diccionario
        valor = (
            random.random()
        )  # Generamos un valor random para introducirle a la clave random

        tiempo_obtencion1 = obtener_tiempo_obtencion(diccionario, clave)
        tiempo_asignacion1 = obtener_tiempo_asignacion(diccionario, clave, valor)

        # Lo introducimos todo en una lista
        tiempos_asignacion.append(tiempo_asignacion1)
        tiempos_obtencion.append(tiempo_obtencion1)
    return tiempos_obtencion, tiempos_asignacion


tamaños_diccionario = [
    100,
    1000,
    10000,
    1000000,
]  # Damos la longitud que queremos que tengan los diccionarios
tiempo_obtencion, tiempo_asignacion = generar_diccionarios(
    tamaños_diccionario
)  # Llamamos a la funcion

# Formateamos el resultado
print(
    "%10s     %10s    %10s" % ("Tamaños", "Tiempo de asignacion", "Tiempo de obtencion")
)
for i in range(len(tamaños_diccionario)):
    print(
        "%10d     %10.3f              %10.3f"
        % (tamaños_diccionario[i], tiempo_asignacion[i], tiempo_obtencion[i])
    )
