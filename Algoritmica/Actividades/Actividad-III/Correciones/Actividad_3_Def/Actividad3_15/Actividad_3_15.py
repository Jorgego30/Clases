from Class_Tablas_Hash import TablaHash

#Se crea la tabla hash
print("Se crea una tabla hash")
H = TablaHash()
#Se le anhaden elementos para comprobar el funcionamiento del nuevo metodo
print(f"Tamanho Tabla Hash: {len(H)}")
print("Se anhade un elemento a la tabla")
H[54] = "insercion1"
print(f"Tamanho Tabla Hash: {len(H)}")
print("Se anhade un elemento a la tabla")
H[26] = "insercion2"
print(f"Tamanho Tabla Hash: {len(H)}")
print("Se anhade un elemento a la tabla")
H[93] = "insercion3"
print(f"Tamanho Tabla Hash: {len(H)}")
print("Se anhade un elemento a la tabla")
H[17] = "insercion4"
print(f"Tamanho Tabla Hash: {len(H)}")
print("Se anhade un elemento a la tabla")
H[77] = "insercion5"
print()
print("Se puede determinar que la complejidad del metodo 'len()' en O(1) porque en todo momento esta devolviendo el valor de una variable, por lo que la complejidad es constante.")