import random
from Class_Impresion import Impresora, Tarea

class Nodo:
    def __init__(self, tarea, prioridad):
        self.tarea = tarea
        self.prioridad = prioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.cabeza = None

    def agregar(self, tarea, prioridad):
        nuevo_nodo = Nodo(tarea, prioridad)
        if self.cabeza is None or prioridad > self.cabeza.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.prioridad >= prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def avanzar(self):
        if self.cabeza is None:
            return None
        tarea = self.cabeza.tarea
        self.cabeza = self.cabeza.siguiente
        return tarea

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def esta_vacia(self):
        return self.cabeza is None

def simulacion(numeroSegundos, paginasPorMinuto):
    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = ColaPrioridad()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):
        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            prioridad = random.randint(1, 5)  # Prioridad aleatoria entre 1 y 5
            colaImpresion.agregar(tarea, prioridad)

        if not impresoraLaboratorio.ocupada() and not colaImpresion.esta_vacia():
            tareaSiguiente = colaImpresion.avanzar()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()

    esperaPromedio = sum(tiemposEspera) / len(tiemposEspera) if tiemposEspera else 0
    print("Tiempo de espera promedio %6.2f segundos  %6.2f minutos  %3d tareas restantes." % (
        esperaPromedio, esperaPromedio / 60, colaImpresion.tamano()))

def nuevaTareaImpresion():
    numero = random.randrange(1, 181)
    return numero == 180

def dame_n():
    while True:
        try:
            n = int(input('Dame el numero de páginas por minuto que quieres que imprima la impresora, debe estar comprendido entre 0 y 10: '))
            if 0 < n < 10:
                return n
        except ValueError:
            print('El valor introducido es invalido, por favor vuelve a intentarlo.')

n = dame_n()
for i in range(10):
    simulacion(3600, n)
