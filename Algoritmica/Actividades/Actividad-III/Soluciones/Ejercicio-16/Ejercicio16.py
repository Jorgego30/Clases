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
