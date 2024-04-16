from Class_Tablas_Hash2 import TablaHash


#Se crea la tabla hash y se anhaden varios elementos de prueba
print("Se crea la tabla y se anhaden 8 elementos")
H = TablaHash()
H[54] = "gato"
H[26] = "perro"
H[93] = "leon"
H[17] = "tigre"
H[77] = "pajaro"
H[31] = "vaca"
H[44] = "cabra"
H[55] = "cerdo"
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
print("Se anhaden mas elementos")
H[20] = "pollo"
H[67] = "caballo"
H[98] = "burro"
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
print(f"Tamanho actual de la tabla: {len(H)}")