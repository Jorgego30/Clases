from Class_Tablas_Hash import *
# Crear una tabla hash
tabla = TablaHash()

# Agregar elementos hasta que la tabla se redimensione automáticamente
for i in range(30):
    tabla[i] = f"Dato {i}"

# Imprimir el tamaño actual de la tabla
print("Tamaño actual de la tabla:", len(tabla))

# Imprimir el contenido de la tabla
for i in range(len(tabla.slots)):
    if tabla.slots[i] is not None:
        print(f"Clave: {tabla.slots[i]}, Dato: {tabla.datos[i]}")

# Agregar más elementos para verificar que la tabla sigue funcionando correctamente
for i in range(30, 50):
    tabla[i] = f"Dato {i}"

# Imprimir el tamaño actual de la tabla después de agregar más elementos
print("Tamaño actual de la tabla después de agregar más elementos:", len(tabla))

# Imprimir el contenido de la tabla después de agregar más elementos
for i in range(len(tabla.slots)):
    if tabla.slots[i] is not None:
        print(f"Clave: {tabla.slots[i]}, Dato: {tabla.datos[i]}")
