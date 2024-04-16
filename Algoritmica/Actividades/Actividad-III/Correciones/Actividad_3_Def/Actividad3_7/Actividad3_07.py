#Importamos las librerías necesarias:
import random
from timeit import Timer

#Definimos una función que va a ir ordenando la función:
def partition(lista, izq, der):
    pivote = lista[der] #Cogemos como pivote el último elemento de la lista
    i = izq - 1
    for j in range(izq, der):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[der] = lista[der], lista[i + 1]
    return i + 1

#Definimos la función para obtener el valor que se encuentra en la posición k:
def obtener_valor(lista, izq, der, k):
    if izq == der:
        return lista[izq]

    #Llamamos a la función que va a ir ordenando la lista:
    pos_pivote = partition(lista, izq, der)

    #Solo ordenamos datos hasta que lleguemos a la posición deseada, no la lista entera:
    if k == pos_pivote:
        return lista[k]
    elif k < pos_pivote:
        return obtener_valor(lista, izq, pos_pivote - 1, k)
    else:
        return obtener_valor(lista, pos_pivote + 1, der, k)

#Creamos una lista de números aleatorios ordenados
def crear_lista(n):
    lista=[]
    for i in range(0,n,1):
        lista.append(random.randint(0,1000))
    return lista

#Preguntamos los datos para el tamaño de la lista y la posición que quieren buscar validando las respuestas:
print("En esta primera parte es recomendable que des un tamaño pequeño de lista porque se imprime por pantalla.")
while True:
    try:
        n=int(input("Dame el tamaño que quieres que tenga la lista: "))
        k=int(input("Dame la posición que quieres buscar (ten en cuenta que se empieza en la posición 0): "))
        if (k>=n):
            print("Esa no es una posición válida (k no puede ser mayor que n). Vuelva a introducir los datos: ")
        else:
            break
    except ValueError:
        print("El valor debía ser numérico y entero. Vuelva a introducirlo")


#Creamos la lista y llamamos a la función;
lista=crear_lista(n)

#Como pasamos lista como lista[:] lo que se pasa es una copia por lo que aunq ordenamos
# no ordenamos la original
valor= obtener_valor(lista[:], 0, len(lista) - 1, k) 

#Comunicamos resultados:
print("Lista antes: ",lista)
print("El elemento en la posición", k, "es:", valor)
print("Lista después (se observa que no se modificó): ",lista)



#Otra función para crear la lista. Esta vez con más opciones de números para que haya menos repetidos
def crear_lista2(n):
    lista=[]
    for i in range(0,n,1):
        lista.append(random.randint(0,100000))
    return lista

#Benchmark para calcular su complejidad temporal:
Obtener=Timer("obtener_valor(lista[:], 0, len(lista) - 1, k)","from __main__ import obtener_valor,lista,k")

#Inicializamos variables:
media=0
contador=0

print("Tamaño \t \t Tiempo \t Valor \t \t Posición")
#Entramos en un bucle que va alterando el tamaño de la lista para hacer diversas pruebas
for j in range(1000,10001,1000):
    lista=crear_lista2(j)
    k=random.randint(0,len(lista)) #Posición que vamos a buscar

    valor= obtener_valor(lista[:], 0, len(lista) - 1, k) #Obtenemos el valor para imprimirlo por pantalla

    t=Obtener.timeit(number=1000) #Calculamos el tiempo que tarda en buscar el elemento

    #Comunicamos los resultados
    print(j," \t ",t," \t ",valor," \t ",k)

    #Calculamos la media temporal
    media+=t
    contador+=1

media=media/contador
#Comunicamos la media:
print()
print("Media: \t ",media)
print()
print("La complejidad temporal de esta función en el caso promedio es de O(n), en el peor caso será de O(n²)")
