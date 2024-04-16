'''Implementa el método tamano (__len__) para la implementación del TAD Vector Asociativo o mapa de las
tablas hash, de manera que sea 𝑶(𝟏𝟏).'''

class TablaHash:
    def __init__(self):
        self.hash_table = {}
        self.size = 0  # Variable para mantener el conteo de elementos

    def __setitem__(self, key, value):
        self.hash_table[key] = value
        self.size += 1

    def __delitem__(self, key):
        if key in self.hash_table:
            del self.hash_table[key]
            self.size -= 1

    def __len__(self):
        return self.size

# Ejemplo de uso
mapa = TablaHash()
mapa['a'] = 1
mapa['b'] = 2

print(len(mapa))  # Salida: 2