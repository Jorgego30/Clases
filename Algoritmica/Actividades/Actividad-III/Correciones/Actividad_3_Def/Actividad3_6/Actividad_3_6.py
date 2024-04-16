import random
import time

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - FUNCIONES DE QUICKSORT - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def quicksort(v, izq, der):
    # inicializacion
    i = izq
    j = der
    pivote = v[random.randint(izq, der)]
    #print(pivote)
    # ciclo principal(particion)
    while i <= j:
        while v[i] < pivote:
            i = i+1
        while v[j] > pivote:
            j = j - 1
        if i <= j:
            tmp = v[i]
            v[i] = v[j]
            v[j] = tmp
            i = i+1
            j = j-1
    # fin ciclo principal
    #print(v)
    # llamadas recursivas
    if izq < j:
        quicksort(v, izq, j)
    if i < der:
        quicksort(v, i, der)
    return(v)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - FUNCION DE CONSEGUIR MAXIMO - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def conseguirmaximorangovector(indice1, indice2, vector):
    '''PROPOSITO FUNCION: Se consigue el maximo de una serie de valores de un vector. Esa serie de valores se encuentran entre 'indice1' e 'indice2'. Esos dos indices tambien se incluyen.'''
    #Se reduce la lista al rango de valores admisibles
    lista = vector[indice1:indice2+1]
    print(f"Se buscara el maximo del rango: {lista}")
    #Se ordena la lista con quicksort
    lista = quicksort(lista, 0, len(lista)-1)
    #Se devuelve el maximo valor
    return lista[-1]
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRAMA PRINCIPAL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Se crea el vector con numeros aleatorios
vector = []
tamanhovector = 15 #Tamanho del vector
for a in range(0,tamanhovector):
    vector.append(random.randint(0,200))
print(f"Busqueda de un maximo en un rango de tipo [indice1, indice2] dentro de un vector de tamanho {tamanhovector}.")
print(f"Vector: {vector}")
#Creacion del rango de busqueda
validado = False
while validado == False:
    try:
        indice1 = input("Inserte el primer valor (indice) del rango en el que quiere realizar la busqueda del maximo: ")
        indice1 = int(indice1)
        if 0 <= indice1 < tamanhovector:
            validado = True
        else:
            print("ERROR. Fuera de rango.")
    except Exception as error:
        print(f"ERROR: {error}")
validado = False
while validado == False:
    try:
        indice2 = input("Inserte el segundo valor (indice) del rango en el que quiere realizar la busqueda del maximo: ")
        indice2 = int(indice2)
        if (0 <= indice2 < tamanhovector) and (indice1 < indice2):
            validado = True
        else:
            print("ERROR. Fuera de rango.")
    except Exception:
        print("ERROR")
#Se llama a la funcion de conseguir maximo
tiempo1 = time.time()
valormaximo = conseguirmaximorangovector(indice1, indice2, vector)
tiempo2 = time.time()
print(f"El valor maximo del vector es: {valormaximo}. Coste temporal: {tiempo2-tiempo1}")