class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def añade(self, elemento, prioridad):
        self.cola.append((elemento, prioridad))

    def primero(self):
        if len(self.cola) == 0:
            return None
        maxima_prioridad = self.cola[0][1]
        maximo_elemento = self.cola[0][0]
        for elemento, prioridad in self.cola:
            if prioridad > maxima_prioridad:
                maxima_prioridad = prioridad
                maximo_elemento = elemento
        return maximo_elemento

    def extrae(self):
        if len(self.cola) == 0:
            return None
        indice = 0
        for i in range(len(self.cola)):
            if self.cola[i][1] > self.cola[indice][1]:
                indice = i
        return self.cola.pop(indice)[0]

    def tamaño(self):
        return len(self.cola)

    def esta_Vacia(self):
        return len(self.cola) == 0


class Impresora:
    def __init__(self, paginas):
        self.tasaPaginas = paginas
        self.colaPrioridad = ColaPrioridad()
        self.tiempoRestante = 0

    def tictac(self):
        if self.tiempoRestante > 0:
            self.tiempoRestante -= 1
            if self.tiempoRestante == 0:
                self.tareaActual = None

    def ocupada(self):
        return self.tiempoRestante > 0

    def iniciarNueva(self, nuevaTarea):
        prioridad = nuevaTarea.obtenerPaginas()  # Utilizamos la cantidad de páginas como prioridad
        self.colaPrioridad.añade(nuevaTarea, prioridad)
        if not self.ocupada():
            self.empezarImpresion()

    def empezarImpresion(self):
        if not self.ocupada() and not self.colaPrioridad.esta_Vacia():
            tarea = self.colaPrioridad.extrae()
            paginas = tarea.obtenerPaginas()
            self.tiempoRestante = paginas * 60 / self.tasaPaginas
            

import random

class Tarea:
    random.seed()
    def __init__(self,tiempo):
        self.marcaTiempo = tiempo
        self.paginas = random.randrange(1,21)

    def obtenerMarca(self):
        return self.marcaTiempo

    def obtenerPaginas(self):
        return self.paginas

    def tiempoEspera(self, tiempoActual):
        return tiempoActual - self.marcaTiempo
