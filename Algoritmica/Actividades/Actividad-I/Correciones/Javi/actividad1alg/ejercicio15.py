''' ejercicio 15: Dada una lista de números en orden aleatorio, escribe un algoritmo que funcione en tiempo O(nlog(n))
para encontrar el k-ésimo número más pequeño de la lista.'''
import random

def quickselect_con_repeticiones(lista, k):
    if not lista:
        return None
    
    # Eliminar elementos duplicados usando un conjunto
    lista_sin_repeticiones = list(set(lista))
    
    # Seleccionar un pivote aleatorio
    pivote = random.choice(lista_sin_repeticiones)
    
    # Particionar la lista en elementos menores, iguales y mayores que el pivote
    menores = [elemento for elemento in lista if elemento < pivote]
    iguales = [elemento for elemento in lista if elemento == pivote]
    mayores = [elemento for elemento in lista if elemento > pivote]
    
    # Recursivamente buscar en la sublista apropiada
    if k < len(menores):
        return quickselect_con_repeticiones(menores, k)
    elif k < len(menores) + len(iguales):
        return pivote
    else:
        return quickselect_con_repeticiones(mayores, k - len(menores) - len(iguales))

# Ejemplo de uso
try:
    # Solicitar al usuario la entrada de la lista de números
    entrada_usuario = input("Introduce la lista de números separados por espacios: ")
    mi_lista = list(map(int, entrada_usuario.split()))

    # Solicitar al usuario el valor de k
    k = int(input("Introduce el valor de k:"))

    # Verificar si k es válido
    if 0 <= k < len(set(mi_lista)):
        # Calcular el k-ésimo elemento más pequeño
        resultado = quickselect_con_repeticiones(mi_lista, k)
        print(f'El {k}-ésimo número más pequeño contando los repetidos como uno solo es: {resultado}')
    else:
        print('El valor de k no es válido para la longitud de la lista.')

except ValueError:
    print('Entrada inválida. Asegúrate de ingresar una lista de números y un valor de k válido.')
