'''Ejercicio 20:

Un ordenamiento burbuja puede modificarse para que “burbujee” en ambas direcciones. La primera pasada
mueve la lista hacia “arriba”, y la segunda pasada la mueve hacia “abajo”. Este patrón alternante continúa
hasta que no son necesarias más pasadas. Implementa esta variación y describe en qué circunstancias podría
ser apropiada.'''

import os
from random import randint
import sys
os.system('clear')

#Creamos una lista aleatoria
def crear_lista_random(tamaño):
    lista_random=[]
    for i in range(tamaño):
        lista_random.append(randint(0,1000))

    return lista_random

#Creamos una función para repetir el proceso si el usuario así lo desea
def repetir():
    Y_N=input('\n\t¿Quieres volver a repetir el programa?[y/n]:')
    Y_N=Y_N.lower()
    while Y_N!= 'y' and Y_N!='n':
        Y_N=input('\n\t¿Quieres volver a repetir el programa?[y/n]:')
        Y_N=Y_N.lower()

    if Y_N=='y':
        main()

    if Y_N=='n':
        print('\n***Gracias por ejecutar el programa***')
        exit(0)

#Realizamos el menú a mostrar al usuario
def elegir_opcion():
    print('\n***ELIGE UNA OPCIÓN***')
    print('\n\tPulsa 1 si deseas realizar un ordenamiento burbuja, ordenando hacia la izquierda.')
    print('\tPulsa 2 si deseas realizar un ordenamiento burbuja, ordenando hacia la derecha.')
    try:
        opcion=int(input('\t'))
        while opcion!=1 and opcion!=2:
            print('***Has cometido un error, inténtalo de nuevo.***\n')
            opcion=elegir_opcion()
        return opcion

    except ValueError:
        print('***Has cometido un error, inténtalo de nuevo.***\n')
        opcion=elegir_opcion()
        return opcion

def ordenamientoBurbuja(unaLista,j):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
    
        j+=1
        print(f'El paso número {j} es: ')
        print(unaLista,'\n')

def ordenamientoBurbuja2(unaLista,j):
    for numPasada in range(0,len(unaLista)+1,1):
        for i in range(1,numPasada):
            for i in range(1,numPasada):
                if unaLista[i]<unaLista[i-1]:
                    temp = unaLista[i]
                    unaLista[i] = unaLista[i-1]
                    unaLista[i-1] = temp
        j+=1
        print(f'El paso número {j} es: ')
        print(unaLista,'\n')

def tamaño_pregunta():
    try:
        tamaño=int(input('¿Cuál quieres que sea el tamaño de la lista?(Recomendación: No pongas una lista muy grande ya que mostrará la lista continuamente): \n'))
        return tamaño
    except:
        print('Has cometido un error, inténtalo de nuevo.\n')
        main()        
    

def main():
    j=0
    tamaño=tamaño_pregunta()
    opcion=elegir_opcion()
    unaLista = crear_lista_random(tamaño)

    if opcion==1:
        ordenamientoBurbuja(unaLista,j)
        repetir()

    if opcion==2:
        ordenamientoBurbuja2(unaLista,j)
        repetir()
  


main()