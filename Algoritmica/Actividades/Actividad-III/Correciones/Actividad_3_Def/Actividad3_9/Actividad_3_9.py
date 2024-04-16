import math
import sys
#sys.set_int_max_str_digits(1000000000)

def triangulopascal2(filas):
    #Funcion que devuelve en una lista los valores del triangulo de pascal. Metodo realizado por recursividad. 
    if filas == 1:
        return [[1]]
    else:
        listacompleta = list(triangulopascal2(filas-1))
        listafilaanterior = listacompleta[-1]
        listafila= []
        for r in range(1,filas+1):
            if r == 1:
                listafila.append(listafilaanterior[0])
            elif r == filas:
                listafila.append(listafilaanterior[-1])
            else:
                listafila.append(listafilaanterior[r-2]+listafilaanterior[r-1])
        listacompleta.append(listafila)
        return listacompleta

def obtencionnumero(triangulo):
    #Funcion que permite obtener una aproximacion del numero e
    resultadomultiplicarfilas = []
    #Se realiza la multiplicacion de todos los elementos de las filas
    for fila in triangulo:
        multiplicacion = 1
        for elemento in fila:
            multiplicacion = multiplicacion * elemento
        resultadomultiplicarfilas.append(multiplicacion)
    #Se realiza la primera division
    listadivision1 = []
    for a in range(1, len(resultadomultiplicarfilas)):
        division = round(resultadomultiplicarfilas[a] / resultadomultiplicarfilas[a-1], 10)
        listadivision1.append(division)
    #Se realiza la segunda division
    listadivision2 = []
    for b in range(1, len(listadivision1)):
        division = round(listadivision1[b] / listadivision1[b-1], 10)
        listadivision2.append(division)
    return listadivision2[-1]


#Programa principal
print("Es necesario esperar varios segundos para obtener el resultado. Obtencion mediante recursividad.")
filas = 700
triangulorecursividad = triangulopascal2(filas)
print(f"La aproximacion del numero e (Utilizando recursividad e iteración) es: {obtencionnumero(triangulorecursividad)}")

