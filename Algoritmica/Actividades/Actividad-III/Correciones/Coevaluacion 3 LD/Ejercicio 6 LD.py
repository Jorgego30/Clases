'''Escribir un algoritmo que obtenga de manera recursiva el valor máximo del tramo [izq; der] de un vector
V. Expresar el coste temporal del algoritmo.'''

def max_valor_tramo_recursivo(V, izq, der):
    if izq == der:
        return V[izq]

    medio = (izq + der) // 2

    # Calcular el máximo en el tramo izquierdo, derecho y que cruza el medio
    max_izq = max_valor_tramo_recursivo(V, izq, medio)
    max_der = max_valor_tramo_recursivo(V, medio + 1, der)

    max_izq_cruz = float('-inf')
    max_der_cruz = float('-inf')
    suma = 0

    for i in range(medio, izq - 1, -1):
        suma += V[i]
        max_izq_cruz = max(max_izq_cruz, suma)

    suma = 0
    for i in range(medio + 1, der + 1):
        suma += V[i]
        max_der_cruz = max(max_der_cruz, suma)

    return max(max_izq, max_der, max_izq_cruz + max_der_cruz)

# Coste temporal del algoritmo: O(n log n), donde n es el tamaño del vector V

# Ejemplo de uso
V = [2, -1, 3, -2, 4, -3, 5, -4]
max_valor = max_valor_tramo_recursivo(V, 0, len(V) - 1)
print(f"El valor máximo del tramo [0; {len(V) - 1}] es: {max_valor}")