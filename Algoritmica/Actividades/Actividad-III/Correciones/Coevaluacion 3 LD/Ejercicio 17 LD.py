'''En la implementación de Vector Asociativo de las tablas hash, se eligió que el tamaño de la tabla hash fuera
11. Si la tabla se llena, ésta debe agrandarse. Implementa el método agregar para que la tabla se
redimensione automáticamente cuando el factor de carga alcance un valor predeterminado (puedes decidir
el valor con base en su apreciación de la carga en función del desempeño).'''

class TablaHash:
    def __init__(self, capacidad, factor_carga_maximo):
        self.capacidad = capacidad
        self.factor_carga_maximo = factor_carga_maximo
        self.cantidad_elementos = 0
        self.hash_table = [[] for _ in range(capacidad)]

    def hash_func(self, key):
        return hash(key) % self.capacidad

    def agregar(self, key, value):
        if (self.cantidad_elementos + 1) / self.capacidad > self.factor_carga_maximo:
            self.redimensionar()
        
        index = self.hash_func(key)
        self.hash_table[index].append((key, value))
        self.cantidad_elementos += 1

    def redimensionar(self):
        nueva_capacidad = self.capacidad * 2
        nueva_tabla = [[] for _ in range(nueva_capacidad)]

        for bucket in self.hash_table:
            for key, value in bucket:
                index = hash(key) % nueva_capacidad
                nueva_tabla[index].append((key, value))

        self.capacidad = nueva_capacidad
        self.hash_table = nueva_tabla

# Ejemplo de uso
mapa = TablaHash(11, 0.7)
for i in range(50):
    mapa.agregar(i, i)

print(mapa.hash_table)