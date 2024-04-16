'''A partir del programa del triángulo de Pascal desarrollado en el ejercicio 3, vamos a multiplicar los
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
explica en este enunciado. Aplicar alguna de las técnicas descritas en el tema…'''

def calcular_aproximacion_e(filas):
    lista_aprox_e = [2]  # Iniciamos con el valor 2
    for i in range(1, filas):
        fila = [1]  # Comenzamos con el primer elemento de cada fila
        for j in range(1, i):
            fila.append(fila[j-1] * (i - j + 1) / j)  # Calculamos los elementos de la fila usando la fórmula del triángulo de Pascal
        resultado_fila = fila[-1]  # Tomamos el último elemento de la fila como resultado
        lista_aprox_e.append(resultado_fila / lista_aprox_e[-1])  # Dividimos entre el resultado de la fila anterior
    return lista_aprox_e

# Número de filas a considerar para el cálculo
filas = 1000

aprox_e = calcular_aproximacion_e(filas)

print(aprox_e[-1])  # Imprimimos la aproximación final de e