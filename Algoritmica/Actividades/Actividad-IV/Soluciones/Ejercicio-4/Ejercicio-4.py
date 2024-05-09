from Class_ArbolesBinariosBusqueda import *

arbol = ArbolBinarioBusqueda()

# Agregar elementos al árbol
print("Agregando elementos al árbol:")
arbol.agregar(50, "A")
arbol.agregar(30, "B")
arbol.agregar(70, "C")
arbol.agregar(20, "D")
arbol.agregar(40, "E")
arbol.agregar(60, "F")
arbol.agregar(80, "G")

# Imprimir el árbol en orden
for clave in arbol:
    print(clave)

# Comprobar la longitud del árbol
print("Longitud del árbol:", len(arbol))

# Comprobar si una clave está en el árbol
print("¿La clave 40 está en el árbol?", 40 in arbol)
print("¿La clave 90 está en el árbol?", 90 in arbol)

# Obtener el valor asociado a una clave
print("Valor asociado a la clave 30:", arbol.obtener(30))
print("Valor asociado a la clave 80:", arbol.obtener(80))

# Eliminar un elemento del árbol
print("Eliminando el elemento con clave 30:")
del arbol[30]

for clave in arbol:
    print(clave)

# Intentar eliminar un elemento que no está en el árbol
try:
    del arbol[90]
except KeyError as e:
    print("Error:", e)

# Agregar un elemento con una clave existente (para actualizar su carga útil)
print("Agregando un elemento con la clave 20 (actualizando su carga útil):")
arbol.agregar(20, "Nuevo D")
for clave in arbol:
    print(clave)