'''¿Cuál es el resultado de ejecutar en orden inverso los dos pasos del método agregar
de la Lista_No_Ordenada? ¿Qué tipo de referencia resultaría? ¿Qué tipos de
problemas pueden resultar?'''

#Importamos las librerias necesarias
import platform
import os

#Funcion para limpiar la pantalla

def limpiar_pantalla ():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

limpiar_pantalla()


class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


class ListaNoOrdenada:

    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self, item): 

        temp = Nodo(item)
        if self.estaVacia():
            self.cabeza = temp
        else:
            actual = self.cabeza
            while actual.obtenerSiguiente() != None:
                actual = actual.obtenerSiguiente()
            actual.asignarSiguiente(temp)


    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
    
        return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
    
        return encontrado

    def borrar(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
    
        if previo == None:
            self.cabeza = actual.obtenerSiguiente()
        else:
            previo.asignarSiguiente(actual.obtenerSiguiente())

    def anexo(self,lista):
        actual = lista.cabeza
        while actual != None:
            self.agregar(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
    
    def fin(self):
        actual = self.cabeza
        while actual.obtenerSiguiente() is not None:
            actual = actual.obtenerSiguiente()
            
        return actual

    def primero(self):
        return self.cabeza

    def siguiente(self, item):
        actual = self.cabeza
        while actual is not None and actual.obtenerDato() != item:
            actual = actual.obtenerSiguiente()
        if actual is not None:
            actual = actual.obtenerSiguiente()
        return actual

    def anterior(self, item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        return previo

miLista = ListaNoOrdenada()
miLista.agregar(1)
miLista.agregar(2)
miLista.agregar(3)

print(miLista)
print(miLista.primero())
print('El tamaño de mi lista es: ',miLista.tamano())