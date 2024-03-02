'''ejercicio 14: Diseña un experimento que compare el desempeño del operador del en listas y en diccionarios.'''

import random

# Generar una lista grande
lista_grande = list(range(1000000))

# Crear un diccionario grande
diccionario_grande = {i: i for i in range(1000000)}

import time

indice_a_eliminar_lista = random.randint(0, len(lista_grande) - 1)

inicio_tiempo_lista = time.time()
del lista_grande[indice_a_eliminar_lista]
tiempo_lista = time.time() - inicio_tiempo_lista

print(f'Tiempo de eliminación en lista: {tiempo_lista} segundos')

llave_a_eliminar_diccionario = random.choice(list(diccionario_grande.keys()))

inicio_tiempo_diccionario = time.time()
del diccionario_grande[llave_a_eliminar_diccionario]
tiempo_diccionario = time.time() - inicio_tiempo_diccionario

print(f'Tiempo de eliminación en diccionario: {tiempo_diccionario} segundos')

