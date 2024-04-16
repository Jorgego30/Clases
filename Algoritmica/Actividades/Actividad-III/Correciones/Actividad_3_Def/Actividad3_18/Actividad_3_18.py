from Class_Tablas_Hash3 import TablaHash


H = TablaHash()
print("Se anhade 1 item")
H[9] = "gato"
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
print("Se anhade 1 item (Es necesario realizar 1 rehash) +1")
H[20] = "perro" #Para este valor es necesario hacer 1 rehash (+1)
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
print("Se anhade 1 item")
H[1] = "leon"
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
print("Se anhade 1 item (Es necesario realizar 1 rehash) +1")
H[12] = "tigre" #Para este valor es necesario hacer 1 rehash (+1)
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
print("Se anhade 1 item (Es necesario realizar 1 rehash) +4")
H[23] = "pajaro" #Para este valor es necesario hacer 2 rehash (+4)
print(f"Lista de slots actual: {H.slots}")
print(f"Lista de datos actual: {H.datos}")
