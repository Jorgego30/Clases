"""
En una tabla hash que utiliza encadenamiento para resolver colisiones, eliminar un elemento implica eliminarlo de la lista enlazada correspondiente al índice calculado para ese elemento. Aquí hay un enfoque paso a paso para eliminar un elemento en una tabla hash con encadenamiento:

Calcular el índice hash del elemento que se desea eliminar.
Ir a la posición en la tabla hash correspondiente a ese índice.
Recorrer la lista enlazada en esa posición y encontrar el elemento que se desea eliminar.
Eliminar el elemento de la lista enlazada.

En el caso del direccionamiento abierto, eliminar un elemento puede ser más complicado, especialmente si se está utilizando una estrategia como sondaje lineal o sondaje cuadrático. En estos métodos, si eliminas un elemento, podrías romper la secuencia de búsqueda y hacer que algunos elementos se vuelvan inaccesibles.

Para manejar estas circunstancias especiales en el direccionamiento abierto, se pueden tomar varias medidas, como marcar los elementos eliminados en lugar de eliminarlos físicamente, reorganizar la tabla hash después de un cierto número de eliminaciones, o utilizar esquemas más complejos como el marcado de tumbas (tombstone marking) para indicar que un elemento ha sido eliminado pero mantener la secuencia de búsqueda intacta. Estas estrategias pueden ser más complicadas de implementar y pueden requerir un mayor costo computacional en comparación con el encadenamiento.
"""

from Class_Tablas_Hash import *


# Crear una tabla hash
tabla = TablaHash()

# Agregar elementos a la tabla
tabla[54] = "manzana"
tabla[26] = "banana"
tabla[93] = "naranja"
tabla[17] = "uva"
tabla[77] = "pera"
tabla[31] = "sandía"
tabla[44] = "cereza"
tabla[55] = "melón"
tabla[20] = "piña"

# Mostrar los elementos de la tabla
print("Tabla Hash después de agregar elementos:")
print(tabla.slots)
print(tabla.datos)

# Obtener un elemento por clave
print("\nObtener elemento con clave 20:", tabla[20])

# Eliminar un elemento por clave
tabla.eliminar(20)
print("\nTabla Hash después de eliminar elemento con clave 20:")
print(tabla.slots)
print(tabla.datos)

# Intentar obtener un elemento eliminado
print("\nIntentar obtener elemento con clave 20 después de eliminarlo:", tabla.obtener(20))
