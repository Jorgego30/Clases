import random
from Class_Impresion import Impresora, Tarea, ColaPrioridad

def simulacion(numeroSegundos, paginasPorMinuto):

    impresoraLaboratorio = Impresora(paginasPorMinuto)
    colaImpresion = ColaPrioridad()
    tiemposEspera = []

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            tarea = Tarea(segundoActual)
            colaImpresion.añade(tarea, tarea.obtenerPaginas())

        if (not impresoraLaboratorio.ocupada()) and (not colaImpresion.esta_Vacia()):
            tareaSiguiente = colaImpresion.extrae()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()

    esperaPromedio = sum(tiemposEspera)/float(len(tiemposEspera))
    esperaPromedioMinutos = esperaPromedio / 60
    tareasRestantes = colaImpresion.tamaño()
    
    print("Tiempo de espera promedio %6.2f segundos %6.2f minutos %3d tareas restantes." % (
        esperaPromedio, esperaPromedioMinutos, tareasRestantes))


def nuevaTareaImpresion():
    numero = random.randrange(1, 181)
    if numero == 180:
        return True
    else:
        return False


for i in range(10):
    simulacion(3600, 5)
