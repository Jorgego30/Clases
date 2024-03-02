from random import *
from timeit import *
import os as os


# Generamos una funcion que borre la pantalla
def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


borrar_pantalla()

def lista_aleatoria(size):
    lista = [randint(0, 19000000) for _ in range(0, size)]
    return lista


def buscar(lista, k):
    lista_apoyo = []
    while len(lista_apoyo) != k:
        apoyo = lista[0]
        for i in range(len(lista)):
            if type(apoyo) == type(lista[i]):
                if lista[i] < apoyo:
                    apoyo = lista[i]
        lista.remove(apoyo)
        lista.append("a")
        lista_apoyo.append(apoyo)

    return apoyo


lista = lista_aleatoria(10000)
# Para ver la lista:
# print(lista)
try:
    k = int(input("Introduce el k-ésimo numero menor que quieres encontrar:"))
except (ValueError, EOFError):
    print("Error al introducir el dato")

print(
    buscar(lista, k),
    "ha tardado en encontrarlo ",
    timeit(lambda: buscar(lista, k), number=1),
    "segundos",
)
