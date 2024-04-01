# Implementar el TAD Colas de Prioridad, usando listas enlazadas ordenadas

from Class_Estructuras_lineales import ColaPrioridad

#Creamos una cola
c = ColaPrioridad()

#Añadimos un par de elemntos a la cola
c.añade(23.34)
c.añade(11)
c.añade(43.23)
c.añade(32)

#Al hacer un print de primero nos dara el número más grande, puesto a que este tiene prioridad
print('\nEl número más grande es:',c.primero())

#Extraemos el más grande y comprobamos que el elemento mayor tomará el puesto de primero
print('\nExtraemos el número más grande: ',c.extrae())

#Ahora que eliminamos el número más grande el siguiente mayor tomará su posición

print('\nAhora el mayor número en la cola es: ',c.primero())

#Prueba a añadir y eliminar números para comprobar que la clase es correcta, 
#pero solo con números, nada de palabras.

