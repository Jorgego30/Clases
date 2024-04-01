# Tema2_12
import random
from Class_Estructuras_lineales import Cola
from Class_Impresion import Impresora, Tarea


def simulacion(numeroSegundos, paginasPorMinuto):
    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = Cola()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.agregar(tarea)

        if (not impresoraLaboratorio.ocupada()) and (not colaImpresion.estaVacia()):
            tareaSiguiente = colaImpresion.avanzar()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()

    esperaPromedio = sum(tiemposEspera)/float(len(tiemposEspera))
    print("Tiempo de espera promedio %6.2f segundos  %6.2f minutos  %3d tareas restantes." % (
        esperaPromedio, esperaPromedio/60, colaImpresion.tamano()))


def nuevaTareaImpresion():
    numero = random.randrange(1, 181)
    if numero == 180:
        return True
    else:
        return False

def dame_n():
    while True:
        try:
            n=int(input('Dame el numero de páginas por minuto que quieres que imprima la impresora, debe estar comprendido entre 0 y 10: '))
            if type(n)==int and 0<n<10:
                return n
        except(ValueError, EOFError):
            print('El valor introducido es invalido, por favor vuelve a intentarlo.')

n=dame_n()
for i in range(10):
    simulacion(3600, n)

