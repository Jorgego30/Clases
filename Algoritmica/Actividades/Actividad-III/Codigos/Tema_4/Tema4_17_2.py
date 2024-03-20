# Tema4_17
def ordenamientoRapido(unaLista):
    ordenamientoRapidoAuxiliar(unaLista, 0, len(unaLista)-1)


def ordenamientoRapidoAuxiliar(unaLista, primero, ultimo):
    if primero < ultimo:

        puntoDivision = particion(unaLista, primero, ultimo)

        ordenamientoRapidoAuxiliar(unaLista, primero, puntoDivision-1)
        ordenamientoRapidoAuxiliar(unaLista, puntoDivision+1, ultimo)


def particion(unaLista, primero, ultimo):
    valorPivote = unaLista[primero]

    marcaIzq = primero+1
    marcaDer = ultimo

    hecho = False
    while not hecho:

        while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
            marcaIzq = marcaIzq + 1

        while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
            marcaDer = marcaDer - 1

        if marcaDer < marcaIzq:
            hecho = True
        else:
            unaLista[marcaIzq],unaLista[marcaDer] = unaLista[marcaDer],unaLista[marcaIzq]

    unaLista[primero],unaLista[marcaDer] = unaLista[marcaDer],unaLista[primero]

    return marcaDer


unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20, 58, 54, 3, 43, 23, 53, 62, 66, 8, 97]
ordenamientoRapido(unaLista)
print(unaLista)
