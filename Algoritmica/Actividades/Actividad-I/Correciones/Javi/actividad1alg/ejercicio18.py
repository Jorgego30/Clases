'''Ejercicio18: Escribir una función que devuelva el número de valores que aparecen dos o más veces en un vector. Calcular
la complejidad temporal de dicha función y expresarla en notación asintótica. ¿Lista o diccionario? Respondiendo a la pregunta: para hacer este ejercicio seria mejor hacer una lista'''

import timeit

def contar_repeticiones(vector):
    frecuencia = {}
    
    for elemento in vector:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1

    repeticiones = sum(1 for valor in frecuencia.values() if valor >= 2)
    
    return repeticiones

def main():
    # Solicitar al usuario la entrada del vector
    entrada_usuario = input("Introduce el vector separado por espacios: ")
    mi_vector = list(map(int, entrada_usuario.split()))

    # Utilizar timeit para medir el tiempo de ejecución
    tiempo_ejecucion_ns = timeit.timeit(lambda: contar_repeticiones(mi_vector), number=1000000)  # number es el número de repeticiones

    # Mostrar resultados
    print(f'Número de valores que aparecen dos o más veces: {contar_repeticiones(mi_vector)}')
    print(f'Tiempo de ejecución: {tiempo_ejecucion_ns * 1e9:.2f} nanosegundos')

if __name__ == "__main__":
    main()
