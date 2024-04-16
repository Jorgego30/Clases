from Class_Tablas_Hash4 import TablaHash

#Se crea la tabla y se anhaden elementos
H = TablaHash()
H[54] = "gato"
H[26] = "perro"
H[110] = "caballo"
H[121] = "burro"
H[93] = "leon"
H[17] = "tigre"
H[77] = "pajaro"
H[31] = "vaca"
H[44] = "cabra"
H[55] = "cerdo"
H[20] = "pollo"
#Se imprime la tabla
print(f"Lista de claves: {H.slots}")
print(f" Lista de datos: {H.datos}")
#Se comprueba la funcion 'obtener'
print(f"Valor de la clave 121: {H.obtener(121)}")
print(f"Valor de la clave 110: {H.obtener(110)}")
print(f"Valor de la clave 77: {H.obtener(77)}")
print(f"Valor de la clave 55: {H.obtener(55)}")
print(f"Valor de la clave 44: {H.obtener(44)}")
print(f"Valor de la clave 26: {H.obtener(26)}")
print(f"Valor de la clave 93: {H.obtener(93)}")
print(f"Valor de la clave 17: {H.obtener(17)}")
print(f"Valor de la clave 31: {H.obtener(31)}")
print(f"Valor de la clave 20: {H.obtener(20)}")
print(f"Valor de la clave 54: {H.obtener(54)}")
#Se comprueba la funcion 'eliminar'
print("Se elimina la clave 121")
H.eliminar(121)
print(f"Lista de claves: {H.slots}")
print(f" Lista de datos: {H.datos}")
print("Se elimina la clave 31")
H.eliminar(31)
print(f"Lista de claves: {H.slots}")
print(f" Lista de datos: {H.datos}")
print("Se elimina la clave 20")
#En la siguiente eliminacion se reinicializa un slot
H.eliminar(20)
print(f"Lista de claves: {H.slots}")
print(f" Lista de datos: {H.datos}")
print("En este caso, para la eliminacion de dichas claves, se realiza una busqueda del item y se procede a eliminarlo. Existe una circustancia especial. Si solo hay un elemento en el slot en el que se va a eliminar el elemento, es necesario reiniciarlo (Se le da el valor [None]). En caso contrario, solo es necesario ejecutar el comando 'del'. En el caso de usar direccionamiento abierto, el algoritmo cambiaria drasticamente.")
