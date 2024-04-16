'''El triángulo de Pascal es un triángulo numérico con números dispuestos en filas escalonadas de manera que
Esta ecuación es la ecuación para un coeficiente binomial. Se puede construir el triángulo de Pascal
agregando los dos números que están, en diagonal, encima de un número en el triángulo. A continuación, se
muestra un ejemplo del triángulo de Pascal.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Escribe, siguiendo técnicas descritas en los apuntes, distintas versiones de un programa que imprima el
triángulo de Pascal. El programa debe aceptar un parámetro que indique cuántas filas se imprimirán del
triángulo.'''

def generar_triangulo_pascal(filas):
    triangulo = []
    for i in range(filas):
        fila = [1] * (i+1)
        if i > 1:
            for j in range(1, len(fila)-1):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        triangulo.append(fila)
    
    return triangulo

def imprimir_triangulo_pascal(triangulo):
    for fila in triangulo:
        print(" ".join(map(str, fila)))

# Número de filas a imprimir
filas = 5

triangulo = generar_triangulo_pascal(filas)
imprimir_triangulo_pascal(triangulo)

def coeficiente_binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return coeficiente_binomial(n-1, k-1) + coeficiente_binomial(n-1, k)

def generar_fila_pascal(n):
    fila = []
    for k in range(n+1):
        fila.append(coeficiente_binomial(n, k))
    return fila

def imprimir_triangulo_pascal(filas):
    for i in range(filas):
        fila = generar_fila_pascal(i)
        print(" ".join(map(str, fila)))

# Número de filas a imprimir
filas = 5

imprimir_triangulo_pascal(filas)