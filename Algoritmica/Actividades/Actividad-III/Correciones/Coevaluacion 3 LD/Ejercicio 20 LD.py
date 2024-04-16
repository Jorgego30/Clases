'''Un ordenamiento burbuja puede modificarse para que “burbujee” en ambas direcciones. La primera pasada
mueve la lista hacia “arriba”, y la segunda pasada la mueve hacia “abajo”. Este patrón alternante continúa
hasta que no son necesarias más pasadas. Implementa esta variación y describe en qué circunstancias podría
ser apropiada.'''

def burbuja_alternante(lista):
    n = len(lista)
    ascendente = True

    while ascendente:
        ascendente = False
        for i in range(0, n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ascendente = True
        
        descendente = False
        for i in range(n-1, 0, -1):
            if lista[i] < lista[i-1]:
                lista[i], lista[i-1] = lista[i-1], lista[i]
                descendente = True

        if not ascendente and not descendente:
            break

    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
resultado = burbuja_alternante(lista)
print("Lista ordenada usando burbuja alternante:", resultado)