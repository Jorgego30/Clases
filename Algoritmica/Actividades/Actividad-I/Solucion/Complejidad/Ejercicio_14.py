import time
import random

def experimento_eliminacion_en_lista(lista, indice):
    inicio = time.time()
    del lista[indice]
    fin = time.time()
    tiempo_eliminacion = fin - inicio
    print(f"Tiempo de eliminación en lista: {tiempo_eliminacion:.10f} segundos")

def experimento_eliminacion_en_diccionario(diccionario, clave):
    inicio = time.time()
    del diccionario[clave]
    fin = time.time()
    tiempo_eliminacion = fin - inicio
    print(f"Tiempo de eliminación en diccionario: {tiempo_eliminacion:.10f} segundos")

tamanio_lista = 1000000
lista = list(range(tamanio_lista))
indice_a_eliminar_en_lista = random.randint(0, tamanio_lista - 1)


tamanio_diccionario = 1000000
diccionario = {i: random.randint(1, 100) for i in range(tamanio_diccionario)}
clave_a_eliminar_en_diccionario = random.choice(list(diccionario.keys()))

experimento_eliminacion_en_lista(lista.copy(), indice_a_eliminar_en_lista)

experimento_eliminacion_en_diccionario(diccionario.copy(), clave_a_eliminar_en_diccionario)
