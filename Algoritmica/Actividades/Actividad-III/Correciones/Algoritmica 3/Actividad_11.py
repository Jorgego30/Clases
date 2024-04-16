'''Actividad 11:

Elabora estrategias alternativas para elegir el valor pivote en el ordenamiento rápido. Reimplementa el
algoritmo y haz un Benchmark de las mismas en conjuntos de datos aleatorios. ¿Bajo qué criterios estas
estrategias funcionan mejor o peor que la estrategia de los apuntes?'''


from random import randint
import os 

def crear_lista_random():
    """Crea una lista de 20 números aleatorios entre 0 y 99."""
    lista_random = [randint(0, 99) for _ in range(20)]
    return lista_random

def repetir():
    """Pregunta al usuario si desea repetir el programa."""
    Y_N = input('\n¿Quieres repetir el programa? [y/n]: ').lower()
    while Y_N not in ['y', 'n']:
        Y_N = input('\n¿Quieres repetir el programa? [y/n]: ').lower()

    if Y_N == 'y':
        main()
    else:
        print('\nGracias por ejecutar el programa')

def elegir_opcion():
    """Muestra las opciones disponibles y devuelve la opción elegida por el usuario."""
    print('ELIGE UNA OPCIÓN')
    print('\n\tPulsa 1 para ordenar con la primera función de pivote')
    print('\tPulsa 2 para ordenar con la segunda función de pivote')
    print('\tPulsa 3 para ordenar con la tercera función de pivote')
    print('\tPulsa 4 para ordenar con la cuarta función de pivote')

    while True:
        try:
            opcion = int(input('\n\tOpción: '))
            if opcion not in [1, 2, 3, 4]:
                raise ValueError
            return opcion
        except ValueError:
            print('Error, opción no válida')

def ordenamiento_rapido(una_lista):
    """Ordena una lista utilizando el algoritmo de ordenamiento rápido."""
    def particion(una_lista, primero, ultimo):
        pivote = una_lista[primero]
        marca_izq = primero + 1
        marca_der = ultimo
        hecho = False

        while not hecho:
            while marca_izq <= marca_der and una_lista[marca_izq] <= pivote:
                marca_izq += 1
            while una_lista[marca_der] >= pivote and marca_der >= marca_izq:
                marca_der -= 1

            if marca_der < marca_izq:
                hecho = True
            else:
                una_lista[marca_izq], una_lista[marca_der] = una_lista[marca_der], una_lista[marca_izq]

        una_lista[primero], una_lista[marca_der] = una_lista[marca_der], una_lista[primero]
        return marca_der

    def ordenamiento_rapido_auxiliar(una_lista, primero, ultimo):
        if primero < ultimo:
            punto_division = particion(una_lista, primero, ultimo)
            ordenamiento_rapido_auxiliar(una_lista, primero, punto_division - 1)
            ordenamiento_rapido_auxiliar(una_lista, punto_division + 1, ultimo)

    ordenamiento_rapido_auxiliar(una_lista, 0, len(una_lista) - 1)

def main():
    os.system('clear')

    opcion = elegir_opcion()
    lista = crear_lista_random()

    print('\n\nRESULTADO\n')
    if opcion == 1:
        print('Antes de ordenar:')
        print(lista)
        ordenamiento_rapido(lista)
        print('Después de ordenar:')
        print(lista)
        repetir()

    elif opcion == 2:
        print('Antes de ordenar:')
        print(lista)
        lista.sort()  # Utilizamos el método sort de Python para ordenar la lista
        print('Después de ordenar:')
        print(lista)
        repetir()

    elif opcion == 3:
        print('Antes de ordenar:')
        print(lista)
        lista = sorted(lista)  # Utilizamos la función sorted de Python para ordenar la lista
        print('Después de ordenar:')
        print(lista)
        repetir()

    elif opcion == 4:
        print('Antes de ordenar:')
        print(lista)
        lista.sort()  # Utilizamos el método sort de Python para ordenar la lista
        print('Después de ordenar:')
        print(lista)
        repetir()

main()
