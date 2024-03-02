''' actividad17:Escribir en lenguaje Python una función que calcule la suma de los elementos de un vector. Calcular la
complejidad temporal de dicha función y expresarla en notación asintótica. Existe algún caso en el que dicha
complejidad pueda ser O(1)? Explícalo: No hay ningun caso en el que el codigo sea de O(1) ya que para hacer la suma es necesario  recorrer siempre la funcion'''

import timeit

def suma_vector(vector):
    suma = 0
    for elemento in vector:
        suma += elemento
    return suma

def main():
    # Solicitar al usuario la entrada del vector
    entrada_usuario = input("Introduce el vector separado por espacios: ")
    mi_vector = list(map(int, entrada_usuario.split()))

    # Utilizar timeit para medir el tiempo de ejecución
    tiempo_ejecucion_ns = timeit.timeit(lambda: suma_vector(mi_vector), number=1000000)  # number es el número de repeticiones

    # Mostrar resultados
    print(f'Suma de los elementos del vector: {suma_vector(mi_vector)}')
    print(f'Tiempo de ejecución: {tiempo_ejecucion_ns * 1e9:.2f} nanosegundos')

if __name__ == "__main__":
    main()
