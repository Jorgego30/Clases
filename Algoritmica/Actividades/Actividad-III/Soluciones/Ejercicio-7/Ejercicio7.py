from random import randint

def crearVector(n):
    vector = []
    for i in range(n):
        vector.append(randint(1, 100))
    return vector

def mediana_divide_y_venceras(vector, inicio, fin, k):
    if inicio == fin:
        return vector[inicio]
    
    # Partición del vector usando el pivote
    pivot = particion(vector, inicio, fin)
    
    # Calcular la posición de la mediana en la partición actual
    pos_pivot = pivot - inicio + 1
    
    # Caso en el que la posición de la mediana está en la partición actual
    if k == pos_pivot:
        return vector[pivot]
    # Si k está a la izquierda del pivote, recursivamente buscar en la partición izquierda
    elif k < pos_pivot:
        return mediana_divide_y_venceras(vector, inicio, pivot - 1, k)
    # Si k está a la derecha del pivote, recursivamente buscar en la partición derecha
    else:
        return mediana_divide_y_venceras(vector, pivot + 1, fin, k - pos_pivot)

def particion(vector, inicio, fin):
    pivot = vector[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if vector[j] <= pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i + 1], vector[fin] = vector[fin], vector[i + 1]
    return i + 1

# Función para calcular la mediana de un vector sin modificarlo
def mediana(vector):
    n = len(vector)
    # La mediana está en la posición (n+1)/2 si n es impar
    # o en las posiciones n/2 y (n/2)+1 si n es par
    if n % 2 == 1:
        return mediana_divide_y_venceras(vector, 0, n - 1, (n + 1) // 2)
    else:
        # Calcula el índice de los dos números centrales
        indice_izquierdo = n // 2
        indice_derecho = n // 2 + 1
        # Calcula la mediana como el promedio de los dos números centrales
        return (mediana_divide_y_venceras(vector, 0, n - 1, indice_izquierdo) + mediana_divide_y_venceras(vector, 0, n - 1, indice_derecho)) // 2


# Ejemplo de uso
longitud = int(input("Introduzca la longitud del vector: "))
vector = crearVector(longitud)
print(f"Tu vector es: {vector}")
print(f"La mediana del vector es: {mediana(vector)}")
