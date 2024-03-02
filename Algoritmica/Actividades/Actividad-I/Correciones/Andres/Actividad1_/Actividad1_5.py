from Class_Fecha import *

import os as os
# Generamos una funcion que borre la pantalla
def borrar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


borrar_pantalla()
try:
    print(Fecha(15,12,1990))
    print(Fecha(30,12,2024))
    print(Fecha.es_menor(Fecha(15,12,1990),Fecha(30,12,2024)))
except(ValueError):
    print("Se ha producido un error al introducir el dia, mes o el año. Por favor intentelo de nuevo")