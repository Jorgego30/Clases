from Clasesp3 import ArbolBinarioBusqueda

# Creamos el árbol binario de búsqueda (ABB) a partir de la lista dada
lista = ['G', 'B', 'Q', 'A', 'C', 'K', 'F', 'P', 'D', 'E', 'R', 'H']
abb = ArbolBinarioBusqueda()
for elemento in lista:
    abb.insertar(elemento)

# Mostramos la evolución de los recorridos
print("Recorrido en preorden:")
abb.recorrido_preorden()

print("Recorrido en inorden:")
abb.recorrido_inorden()

print("Recorrido en postorden:")
abb.recorrido_postorden()

print("Recorrido en anchura:")
abb.recorrido_anchura()

# Verificamos los algoritmos para determinar la cantidad de nodos, el número de hojas y la profundidad
print("\nCantidad de nodos del árbol:", abb.cantidad_nodos())
print("Número de hojas del árbol:", abb.cantidad_hojas())
print("Profundidad del árbol:", abb.profundidad())
