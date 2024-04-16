'''
Ejercicio 17.
En la implementación de Vector Asociativo de las tablas hash, se eligió que el tamaño de la tabla hash fuera
11. Si la tabla se llena, ésta debe agrandarse. Implementa el método agregar para que la tabla se
redimensione automáticamente cuando el factor de carga alcance un valor predeterminado (puedes decidir
el valor con base en su apreciación de la carga en función del desempeño)'''

from Class_Hash import * #importamos la clase de la tabla hash
import os 
os.system('clear')

print('Primero vamos a crear una tabla hash que no supere la dimension 11:\n')

H = TablaHash()#creamos una tabla hash y la mostramos
H[26] = "perro"
H[93] = "leon"
H[17] = "tigre"
H[77] = "pajaro"
H[31] = "vaca"
H[44] = "cabra"
H[55] = "cerdo"
H[20] = "pollo"
H[45] = "caballo"
H[21] = "cabra"

print(H.slots) #mostramos la tabla hash creada y su volumen de carga
print(H.datos)
print('el volumen de carga de esta tabla es: ', len(H))
print("\nAhora vamos a meter más datos en la tabla, haciendo que se supere la capacidad de carga de la tabla. Esto ocasionará que se redimensione y reordene automáticamente.")


H[69]= "plosplos" #añadimos más datos a la tabla para que se supere la capacidad de carga
H[70]= "jose"
H[64]= "juan"
H[34]= "macaco"
H[25]= "dragon"
print('\nLa tabla con los nuevos datos es: \n',H.slots,'\n',H.datos) #mostramos la nueva tablas hash
print('\nEl volumen de carga de esta tabla es: ', len(H)) #mostramos la capacidad de carga de la tabla