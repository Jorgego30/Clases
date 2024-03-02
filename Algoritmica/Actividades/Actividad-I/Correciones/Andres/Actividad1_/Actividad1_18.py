'''
En cuanto a la elección entre lista o diccionario, 
el enfoque utilizado en el código siguiente utiliza un
diccionario para mantener un registro de las frecuencias 
de cada elemento. Esto permite verificar fácilmente si un 
elemento ya ha aparecido. Si bien podrías implementar una 
solución con una lista, la búsqueda en una lista tiene una 
complejidad O(n)O(n), lo que haría que la solución en su 
conjunto fuera menos eficiente en términos de tiempo.  
Utilizar un diccionario es más eficiente en este caso.
'''
def contar_duplicados(vector):
    frecuencia = {}
    duplicados = 0

    for elemento in vector:
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1

    for valor, cantidad in frecuencia.items():
        if cantidad >= 2:
            duplicados += 1

    return duplicados

def pedir_vector():
    try:
        # Solicitar al usuario que ingrese los elementos del vector
        entrada = input("Ingresa los elementos del vector separados por espacios: ")

        # Convertir la entrada en una lista de números enteros
        vector = [int(x) for x in entrada.split()]

        return vector
    except ValueError:
        print("Error: Ingresa solo números enteros.")
        return pedir_vector()

vector = pedir_vector()
print(contar_duplicados(vector))

