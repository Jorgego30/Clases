'''
Ejercicio 18.
Implementa la prueba cuadrática como una técnica de rehash.'''

from Class_18 import * #importamos la clase de la tabla hash
import os 
os.system('clear')

H = TablaHash() #iniciamos una tablas hash y metemos datos en ella
H[11] = "gato"
H[44] = "perro"
H[55] = "leon"
H[22] = "tigre"
H[77] = "pajaro"
H[79] = "vaca"
H[58] = "cabra"
H[43] = "cerdo"
H[20] = "pollo"
H[73]='pipo'

print(H.slots) #mostramos la tabla hash creada
print(H.datos)

print('\nLo que ocurre en este ejercicio es que los elentos con las claves 11,44,22y 55 tienen el mismo resto al dividir con el tamaño de la tabla\npor lo que todos buscan ocupar la misma posición, como esto no es posible se rehasean según la prueba cuadrática (osea que oacuparían la posición 1,4,9...')