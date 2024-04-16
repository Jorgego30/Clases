'''
Actividad 6: 


Escribir un algoritmo que obtenga de manera recursiva el valor máximo del tramo [izq; der] de un vector
V. Expresar el coste temporal del algoritmo.
'''

def maximo_tramo_recursivo(V, izq, der):
    # Caso base: Si solo hay un elemento en el tramo, se devuelve ese elemento
    if izq == der:
        return V[izq]
    
    # Se calcula el punto medio del tramo
    medio = (izq + der) // 2
    
    # Se calcula el máximo en el tramo izquierdo recursivamente
    max_izq = maximo_tramo_recursivo(V, izq, medio)
    # Se calcula el máximo en el tramo derecho recursivamente
    max_der = maximo_tramo_recursivo(V, medio + 1, der)
    
    # Se devuelve el máximo entre el máximo del tramo izquierdo y el máximo del tramo derecho
    return max(max_izq, max_der)


vector = [4, -3, 5, -2, -1, 2, 6, -2, 8]
# Se llama a la función maximo_tramo_recursivo para encontrar el valor máximo en el vector dado
resultado = maximo_tramo_recursivo(vector, 0, len(vector) - 1)
print("El valor máximo del tramo es:", resultado)


#Al ser un algoritmo que utiliza la estrategia de divide y vencerás tiene O(log(n))