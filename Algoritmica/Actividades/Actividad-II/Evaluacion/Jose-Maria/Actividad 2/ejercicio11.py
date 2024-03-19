'''. Implementar los métodos no desarrollados en el TAD Lista_No_Ordenada, así como
los métodos fin, primero, siguiente y anterior'''

#Importamos las librerias necesarias 

from class_estructuras_lineales import ListaNoOrdenada
import platform
import os

#Funcion para limpiar la pantalla

def limpiar_pantalla ():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

limpiar_pantalla()

milista = ListaNoOrdenada()
milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)
print(milista.tamano())
print(milista.buscar(93))
print(milista.buscar(100))
milista.agregar(100)
print(milista.buscar(100))
print(milista.tamano())
milista.borrar(54)
print(milista.tamano())
milista.borrar(93)
print(milista.tamano())
milista.borrar(31)
print(milista.tamano())
print(milista.buscar(93))

milista2 = ListaNoOrdenada()
milista2.agregar(20)
milista2.agregar(1000)
milista2.agregar(1000)

milista3 = ListaNoOrdenada()
milista3.agregar(1)
milista3.agregar(2)
milista3.agregar(3)
milista3.agregar(4)
milista3.agregar(5)
milista3.agregar(6)

milista2.anexo(milista)

x=milista3.fin()
print("El último elemento de milista3 es:", x.obtenerDato())

z=milista3.primero()
print('El primer elemento de milista3 es: ',z.obtenerDato())

y=milista3.siguiente(2)
print('El elemento de milista3 siguiente al número 2 es: ',y.obtenerDato())

t=milista3.anterior(2)
print('El elemento de milista3 anterior al número 2 es: ',t.obtenerDato())