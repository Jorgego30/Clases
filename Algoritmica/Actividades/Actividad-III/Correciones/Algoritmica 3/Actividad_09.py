'''Actividad 9:

A partir del programa del triángulo de Pascal desarrollado en el ejercicio 3, vamos a multiplicar los
elementos de cada una de las filas:
Si ahora dividimos cada resultado obtenido al multiplicar entre el obtenido en la fila anterior obtenemos los
siguientes valores:
{1, 2, 4.5, 10.666, …, 26.0417, 64.8}
Y ahora volvamos a dividir cada uno de los resultados de esa lista entre el anterior. Llegamos a los siguientes
datos:
{2, 2.25, 2.370370, … , 2.44140625, 2.48832}
Parece que después de comenzar en 2 los números van subiendo poco a poco. Si avanzamos un poco, por
ejemplo, por la zona del n=1000, el dato de la lista sería ya 2.71692, que ya está más cerca del número e
=2.71818281
Modifica el programa realizado en el ejercicio 3 para que calcule una aproximación del número e tal y como se
explica en este enunciado. Aplicar alguna de las técnicas descritas en el tema…
'''


lista = []

def crear_triangulo(n):
    global lista  # Se declara global para que se pueda modificar dentro de la función
    global max
    espacios = " "
    if n == 1:
        fila = [1]
        print(espacios*(max-n) + str(fila))  # Ajuste de espacios
    else:
        fila_anterior = crear_triangulo(n-1)  # llama a crear_triangulo con n-1 filas para obtener la lista de la fila n-1
        fila = [None]*n
        fila[0] = 1
        fila[n-1] = 1

        for i in range(1,n-1):  # iterar para los n elementos de la fila
            fila[i] = fila_anterior[i] + fila_anterior[i-1]  # calcular el elemento n-esimo en funcion de la fila n-1 anterior

        espacios = espacios * (max-n)  # Ajuste de espacios
        print(espacios + str(fila))
    
    lista.extend(fila)  # Se agregan los elementos de la fila a la lista global
    return fila

def resultado_lista():
    global lista
    lista_divisiones = []
    lista_divisiones1 = []

    for i in range(1,len(lista)):
        divisiones = lista[i]/lista[i-1]
        lista_divisiones.append(divisiones)

    for i in range(1,len(lista_divisiones)):
        divisiones = lista_divisiones[i]/lista_divisiones[i-1]
        lista_divisiones1.append(divisiones)

    print("la lista resultante de dividir cada elemento entre el anterior es: ",lista_divisiones,"\n")
    print("la lista resultante de dividir nuevamente cada elemento entre el anterior es: ",lista_divisiones1,"\n")

max = int(input("Introduce las filas del triángulo de Pascal: "))

# llamar a la funcion recursiva que calcule y dibuje el triangulo
triangulo = crear_triangulo(max)
print("la lista resultante de multiplicar los elementos de cada fila es: \n")
resultado_lista()

