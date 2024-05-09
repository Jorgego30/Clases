from Class_Monticulos import *
import time

def heap_sort(lista):
    # Crear un objeto de MonticuloBinario
    monticulo = MonticuloBinario()
    
    # Construir un montículo a partir de la lista
    monticulo.construirMonticulo(lista)
    
    # Lista para almacenar los elementos ordenados
    elementos_ordenados = []
    
    # Extraer el mínimo del montículo y agregarlo a la lista de elementos ordenados
    for _ in range(len(lista)):
        elementos_ordenados.append(monticulo.eliminarMin())
    
    return elementos_ordenados

# Ejemplo de uso
lista_desordenada = [9, 5, 7, 2, 3, 6, 1, 8, 4]
print("Lista original:", lista_desordenada)
inicio = time.time()
lista_ordenada = heap_sort(lista_desordenada)
fin = time.time()
print("Lista ordenada:", lista_ordenada)
tiempo_ordenacion = fin - inicio
print(f"Tiempo de ordenacion de la lista: {tiempo_ordenacion:.10f} segundos")
