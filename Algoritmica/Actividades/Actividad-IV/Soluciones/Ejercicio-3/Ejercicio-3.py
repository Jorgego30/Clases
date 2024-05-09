from Class_ArbolesBinariosBusqueda import *
# Función para probar todos los métodos de la clase ArbolBinarioBusqueda
def probar_arbol_binario():
    # Crear un árbol binario de búsqueda
    arbol = ArbolBinarioBusqueda()

    # Agregar elementos al árbol
    arbol.agregar(50, "A")
    arbol.agregar(30, "B")
    arbol.agregar(70, "C")
    arbol.agregar(20, "D")
    arbol.agregar(40, "E")
    arbol.agregar(60, "F")
    arbol.agregar(80, "G")

    # Obtener la longitud del árbol
    print("Longitud del árbol:", len(arbol))

    # Iterar sobre el árbol utilizando un bucle for
    print("Recorrido inorden utilizando el método __iter__:")
    for clave in arbol:
        print(clave)

    # Realizar el recorrido inorden no recursivo
    print("Recorrido inorden no recursivo:")
    for clave in recorrido_inorden_no_recursivo(arbol):
        print(clave)

    # Prueba de la operación de indexación (__getitem__)
    print("Obtener el valor para la clave 40:", arbol[40])

    # Verificar si una clave está presente en el árbol
    print("¿La clave 60 está en el árbol?", 60 in arbol)

    # Eliminar un elemento del árbol
    print("Eliminando la clave 30...")
    del arbol[30]

    # Verificar si la clave eliminada sigue en el árbol
    print("¿La clave 30 está en el árbol?", 30 in arbol)

    # Obtener la longitud actualizada del árbol
    print("Longitud del árbol después de eliminar un elemento:", len(arbol))

    # Iterar sobre el árbol después de eliminar un elemento
    print("Recorrido inorden después de eliminar un elemento:")
    for clave in arbol:
        print(clave)

# Ejecutar la función de prueba
probar_arbol_binario()
