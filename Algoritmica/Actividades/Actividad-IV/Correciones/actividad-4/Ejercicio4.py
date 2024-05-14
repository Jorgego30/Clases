#Modifica la implementación de árbol binario de búsqueda para que maneje correctamente claves
#duplicadas. Es decir, si una clave ya está en el árbol, entonces la nueva carga útil debería sustituir a la
#antigua en lugar de agregar otro nodo con la misma clave.


from Class_ArbolesBinariosBusqueda import *

arbol = ArbolBinarioBusqueda()

arbol.agregar(0,19)
arbol.agregar(3,21)
arbol.agregar(4,22)
arbol.agregar(4,23)
arbol.agregar(5,11)

print("Valor del arbol con la clave 4 sustituyendo la nueva por la antigua: ")
print(arbol.obtener(4))