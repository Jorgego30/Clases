'''
Complejidad temporal en notación asintótica (Big O): O(n)O(n), donde
n es la longitud del vector.

La función realiza una iteración sobre cada elemento del vector,
 por lo que el tiempo de ejecución crece linealmente con el tamaño del vector.

No es posible tener una complejidad O(1)O(1) (constante) para la suma de todos
los elementos en un vector, ya que necesitas pasar por cada elemento para
sumarlos. La complejidad O(1)O(1) generalmente se asocia con operaciones
de tiempo constante, pero en este caso, la cantidad de operaciones aumenta 
linealmente con el tamaño del vector, lo que resulta en una complejidad 
O(n)O(n). Esto lo podríamos solucinar si sabemos la longitud del vector
y así resolverlo por indexación.
'''

def suma_vector(vector):
    suma = 0
    for elemento in vector:
        suma += elemento
    return suma
