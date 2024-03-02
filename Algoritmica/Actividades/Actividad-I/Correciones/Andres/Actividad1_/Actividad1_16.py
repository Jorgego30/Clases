from random import randint
from timeit import timeit
import os as os


# Generamos una funcion que borre la pantalla
def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


borrar_pantalla()

def seleccion_rapida(lista, k):
    if len(lista) == 1:
        return lista[0]

    pivot = lista[randint(0, len(lista)-1)]
    menores = [x for x in lista if x < pivot]
    iguales = [x for x in lista if x == pivot]
    mayores = [x for x in lista if x > pivot]

    if k < len(menores):
        return seleccion_rapida(menores, k)
    elif k < len(menores) + len(iguales):
        return iguales[0]
    else:
        return seleccion_rapida(mayores, k - len(menores) - len(iguales))

# Ejemplo de uso:
lista = [randint(0,10000) for _ in range(1000)]#Aumenta la variable del bulce para que la lista sea mas grande
#print(lista)
try:
    k = int(input("Introduce la K para el K-ésimo numero que de la lista que quieras encontar: "))
    if k<0:
        print("Error al introucir el numero, debe ser un numero entero y mayor que 0.")

except(ValueError) :
    print("Error al introucir el numero, debe ser un numero entero y mayor que 0.")

print(f"El {k}-ésimo número más pequeño en la lista es: {seleccion_rapida(lista, k-1)} y el tiempo que ha tardado ha sido de:{timeit(lambda:seleccion_rapida(lista, k-1),number=1)}")