from Class_ListaEnlazada import *

lista = ListaEnlazada()

#Ejemplo de los metodos para insertar numeros al inicio y al final
lista.insertar_al_inicio(1)
lista.insertar_al_inicio(2)
lista.insertar_al_final(3)
lista.insertar_al_final(4)

# Salida: 2 1 3 4
lista.imprimir_lista()  

#Ejemplo del metodo de eliminar algo de la lista
lista.eliminar(3)

# Salida: 2 1 4
lista.imprimir_lista()  

#Ejemplo de la salida de la lista invertida pr recursividad
lista.invertir_recursivamente(lista.cabeza)
lista.imprimir_lista()