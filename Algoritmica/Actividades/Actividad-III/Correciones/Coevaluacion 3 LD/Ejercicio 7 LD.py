'''Dado un vector V de longitud n, aplicando el esquema de diseño Divide y vencerás y sin modificar V,
escribir una función que devuelva el valor que ocuparía la posición k (p.e. posición de la mediana) si el
vector V estuviera ordenado. Calcular su complejidad temporal en función de n y expresarla en notación
asintótica.'''

import random

def valor_ordenado_posicion_k(V, k):
    if k >= 0 and k < len(V):
        return quickselect(V, 0, len(V) - 1, k)
    else:
        return None

def quickselect(V, izq, der, k):
    if izq == der:
        return V[izq]

    pivote = particion(V, izq, der)

    if k == pivote:
        return V[k]
    elif k < pivote:
        return quickselect(V, izq, pivote - 1, k)
    else:
        return quickselect(V, pivote + 1, der, k)

def particion(V, izq, der):
    pivote = random.randint(izq, der)
    V[izq], V[pivote] = V[pivote], V[izq]
    pivote = izq
    i = izq + 1

    for j in range(izq + 1, der + 1):
        if V[j] < V[izq]:
            pivote += 1
            V[j], V[pivote] = V[pivote], V[j]

    V[izq], V[pivote] = V[pivote], V[izq]
    return pivote

# Complejidad temporal en notación asintótica: O(n) en el peor caso

# Ejemplo de uso
V = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 5
valor_mediana = valor_ordenado_posicion_k(V, k)
print(f"El valor que ocuparía la posición {k} si el vector estuviera ordenado es: {valor_mediana}")