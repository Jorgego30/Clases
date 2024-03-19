#Realiza la especificación informal del TAD Cola Doble

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


class ColaDoble:
    def __init__(self): #init(): Efecto: Crea una cola doble vacía. 
        self.items = []

    def __str__(self): #str(): Requerimiento: No tiene requerimientos. Efecto: Devuelve una cadena de caracteres que representa la cola doble.
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self): #estaVacia(): Requerimiento: La Coladoble Efecto: Devuelve True si la cola doble está vacía y False en caso contrario.
        return self.items == []

    def agregarFrente(self, item): #Requerimiento: Una coladoble y un item. Efecto: Agrega el elemento item al frente de la cola doble.
        self.items.append(item)

    def agregarFinal(self, item): ##Requerimiento: Una coladoble y un item. Efecto: Agrega el elemento item al final de la cola doble.
        self.items.insert(0,item)

    def borrarFrente(self): #Requerimiento: La coladoble. Efecto: Elimina y devuelve el elemento del frente de la cola doble.
        return self.items.pop()

    def borrarFinal(self): #Requerimiento: La coladoble. Efecto: Elimina y devuelve el elemento del final de la cola doble.
        return self.items.pop(0)

    def tamano(self): #Requerimiento: La coladoble. Efecto: Devuelve la cantidad de elementos en la cola doble (int).
        return len(self.items)
    
    def frente (self): #Requerimiento: La coladoble. Efecto: Devuelve el elemento del frente de la cola doble sin eliminarlo.
        return self.items[len(self.items)-1]

    def ultimo (self): ##Requerimiento: La coladoble. Efecto: Devuelve el elemento del final de la cola doble sin eliminarlo.
        if len(self.items)>0:
            return self.items[0]
    
    def inspeccionar(self, index): #Requerimiento: el índice y la coladoble. Efecto: Devuelve el elemento en la posición index de la cola doble sin eliminarlo.
        return self.items[index]


'''     init(): Crea una cola doble vacía.
        str(): Devuelve una cadena de caracteres que representa la cola doble.
        estaVacia(): Devuelve True si la cola doble está vacía y False en caso contrario.
        agregarFrente(item): Agrega el elemento item al frente de la cola doble.
        agregarFinal(item): Agrega el elemento item al final de la cola doble.
        borrarFrente(): Elimina y devuelve el elemento del frente de la cola doble.
        borrarFinal(): Elimina y devuelve el elemento del final de la cola doble.
        tamano(): Devuelve la cantidad de elementos en la cola doble.
        frente(): Devuelve el elemento del frente de la cola doble sin eliminarlo.
        ultimo(): Devuelve el último elemento de la cola doble sin eliminarlo.
        inspeccionar(index): Devuelve el elemento en la posición index de la cola doble sin eliminarlo.'''