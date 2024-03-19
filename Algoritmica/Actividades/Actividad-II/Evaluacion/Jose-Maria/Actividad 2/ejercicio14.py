'''Para implementar el método tamano contamos el número de nodos en la lista. Una
estrategia alternativa sería almacenar el número de nodos en la lista como una pieza
de datos adicional en la cabeza de la lista. Modifica la clase ListaNoOrdenada para
incluir esta información y reescribe el método tamano. ¿Qué complejidad tiene el
método tamano ahora'''

#Importamos las librerias necesarias 
from class_nodos import *
import platform
import os

#Funcion para limpiar la pantalla

def limpiar_pantalla ():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

limpiar_pantalla()
class ListaNoOrdenada:
    """
        Los valores del TAD Lista son listas de items del tipo tipoelem.
        Las posiciones de los items de la lista y la posición fin de la lista 
        son del tipo int.
        Las listas son mutables: agregar, insertar, anexar, borrar y modificar,
        añaden, eliminan y modifican items en la lista.
    """

    def __init__(self):
        """
            efecto: Crea y devuelve la lista vacía
        """
        self.cabeza = None

    def estaVacia(self):
        """
            requerimientos: Una lista 
            efecto: Devuelve TRUE si es lista vacía, y FALSE en caso contrario
        """
        return self.cabeza == None
    
    def agregar(self,item):
        """
            requerimientos: Una lista y un item
            modifica: La lista
            efecto: Inserta el item en la lista como primer item de la lista.

        """
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def buscar(self,item):
        """
            requerimientos: Una lista no vacía y el ítem a buscar
            efecto: Devuelve TRUE si esta en la lista y FALSE en caso contrario. 
        """
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
    
        return encontrado

    def borrar(self,item):
        """
            requerimientos: Una lista no vacía y un item
            modifica: La lista
            efecto: Elimina el item de la lista

        """
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
    
    def anexar(self, item):
            """
                requerimientos: Una lista y un item
                modifica: La lista
                efecto: Añade el item al final de la lista
            """
            temp = Nodo(item)
            if self.cabeza is None:
                self.cabeza = temp
            else:
                actual = self.cabeza
                while actual.obtenerSiguiente() is not None:
                    actual = actual.obtenerSiguiente()
                actual.asignarSiguiente(temp)

    def indice(self, item):
            """
                requerimientos: Una lista no vacía y un item
                efecto: Devuelve la posición del item en la lista o None si el item no está en la lista
            """
            actual = self.cabeza
            posicion = 0
            encontrado = False
            while actual is not None and not encontrado:
                posicion += 1
                if actual.obtenerDato() == item:
                    encontrado = True
                else:
                    actual = actual.obtenerSiguiente()
            if encontrado:
                return posicion
            else:
                return None

    def extraer(self):
            """
                requerimientos: Una lista no vacía
                modifica: La lista
                efecto: Elimina y devuelve el último item de la lista o None si la lista está vacía
            """
            actual = self.cabeza
            previo = None
            if actual is None:
                return None
            if actual.obtenerSiguiente() is None:
                temp = actual
                self.cabeza = None
                return temp.obtenerDato()
            while actual.obtenerSiguiente() is not None:
                previo = actual
                actual = actual.obtenerSiguiente()
            temp = actual
            previo.asignarSiguiente(None)
            return temp.obtenerDato()

    def extraer_pos(self, pos):
            """
                requerimientos: Una lista no vacía y una posición válida (1 <= pos <= tamaño de la lista)
                modifica: La lista
                efecto: Elimina y devuelve el item en la posición dada de la lista o None si la posición es inválida
            """
            if pos < 1 or pos > self.tamano():
                return None
            actual = self.cabeza
            previo = None
            for i in range(pos-1):
                previo = actual
                actual = actual.obtenerSiguiente()
            if previo is None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
            return actual.obtenerDato()

    def modificar(self, pos, item):
        """
                requerimientos: Una lista no vacía y una posición válida (1 <= pos <= tamaño de la lista)
                modifica: La lista
                efecto: Modifica el item en la posición dada de la lista con el item dado y devuelve True, 
                        o devuelve False si la posición es inválida
        """
        if pos < 1 or pos > self.tamano():
                return False
        actual = self.cabeza
        for i in range(pos-1):
                actual = actual.obtenerSiguiente()
        actual.asignarDato(item)
        return True 
    
    def insertar(self, pos, item):
        """
            requerimientos: Una lista no vacía, una posición válida y un item
            modifica: La lista
            efecto: Inserta el item en la posición indicada
        """
        if pos == 0:
            self.agregar(item)
        else:
            actual = self.cabeza
            previo = None
            i = 0
            while actual != None and i < pos:
                previo = actual
                actual = actual.obtenerSiguiente()
                i = i + 1
    
            if i == pos:
                temp = Nodo(item)
                temp.asignarSiguiente(actual)
                previo.asignarSiguiente(temp)
            else:
                raise IndexError("Posición fuera de rango")
    
    def anexar_lista(self, otra_lista):#Tiene comlejidad temporal O
            for elemento in otra_lista:
                self.agregar(elemento)
    #Esto es solo para poder ver la lista anexada
    def imprimirLista(self):
        """
        requerimientos: Una lista no vacía
        efecto: Imprime los elementos de la lista en orden.
        """
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSiguiente()
#Nuevo  metodo tamaño con complejidad temporal O(1)
    def tamano(self):
        return self.tamano
    
miLista = ListaNoOrdenada()
miLista.agregar(1)
miLista.agregar(2)
miLista.agregar(3)

print(miLista)
print('El tamaño de mi lista es: ',miLista.tamano())