'''Implementa la prueba cuadrática como una técnica de rehash.'''


class TablaHash:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.hash_table = [None] * capacidad

    def hash_func(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key, value):
        index = self.hash_func(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = (key, value)
        else:
            # Resolución de colisión mediante prueba cuadrática
            i = 1
            while True:
                new_index = (index + i**2) % self.capacidad
                if self.hash_table[new_index] is None:
                    self.hash_table[new_index] = (key, value)
                    break
                i += 1

# Ejemplo de uso
mapa = TablaHash(11)
mapa.agregar('a', 1)
mapa.agregar('b', 2)
mapa.agregar('c', 3)

print(mapa.hash_table)