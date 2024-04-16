'''¿Cómo puedes eliminar ítems de una tabla hash que utiliza encadenamiento para la solución de colisiones?
¿Qué tal si se usa direccionamiento abierto? ¿Cuáles son las circunstancias especiales que deben manejarse?
Implementa el método eliminar para la clase TablaHash que utiliza encadenamiento.'''

class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.hash_table = [[] for _ in range(capacidad)]

    def hash_func(self, key):
        return hash(key) % self.capacidad

    def insertar(self, key, value):
        index = self.hash_func(key)
        self.hash_table[index].append((key, value))

    def eliminar(self, key):
        index = self.hash_func(key)
        bucket = self.hash_table[index]
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                return

# Ejemplo de uso
mapa = TablaHash(10)
mapa.insertar('a', 1)
mapa.insertar('b', 2)

mapa.eliminar('a')

print(mapa.hash_table)