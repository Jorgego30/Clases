from Class_Tablas_Hash import *

# Creamos una instancia de la tabla hash
tabla = TablaHash()

# Agregamos algunos elementos
tabla[54] = 'manzana'
tabla[26] = 'banana'
tabla[93] = 'sandía'
tabla[17] = 'uva'
tabla[77] = 'naranja'
tabla[31] = 'pera'
tabla[44] = 'limón'
tabla[55] = 'cereza'

# Mostramos algunos elementos
print("Elemento asociado a la clave 17:", tabla[17])
print("Elemento asociado a la clave 44:", tabla[44])

# Intentamos acceder a un elemento que no está en la tabla
print("Elemento asociado a la clave 100:", tabla[100])  # Debería devolver None

# Intentamos agregar un elemento con una clave existente
tabla[44] = 'piña'

# Mostramos el contenido de la tabla hash
print("\nContenido de la tabla hash:")
for i in range(tabla.tamano):
    if tabla.slots[i] is not None:
        print(f"Clave: {tabla.slots[i]}, Valor: {tabla.datos[i]}")
    else:
        print("Posición vacía")
