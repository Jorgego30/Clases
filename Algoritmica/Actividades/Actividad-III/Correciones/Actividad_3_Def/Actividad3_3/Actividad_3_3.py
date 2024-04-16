import math

def triangulopascal1(filas):
    #Funcion que devuelve en una lista los valores del triangulo de pascal. Metodo realizado por iteracion. 
    #n-> filas
    #r-> columna
    listacompleta = []
    for n in range(0,filas):
        fila = []
        for r in range(0,n+1):
            res = int(math.factorial(n) / (math.factorial(r)*math.factorial(n-r)))
            fila.append(res)
        listacompleta.append(fila)
    return listacompleta

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

def imprimirtriangulopascal(triangulo):
    #Funcion que imprime de una manera estetica el triangulo de pascal
    nfila = 0
    for n in triangulo:
        #print(n)
        fila = "  "* (len(triangulo)-nfila)
        for r in n:
            #print(r)
            if r< 10:
                fila = f"{fila}  0{r}"
            else:
                fila = f"{fila}  {r}"
        print(fila)
        nfila += 1

#Programa principal
validado = False
while validado != True:
    try:
        filas = int(input("Indique el numero de filas del triangulo de pascal: "))
        validado = True
    except Exception:
        print("Error")
#Imprime los dos triangulos como tipo de lista
print("Lista de valores del triangulo de pascal realizado por iteracion: ")
trianguloiteracion = triangulopascal1(filas)
print(trianguloiteracion)
print("Lista de valores del triangulo de pascal realizado por recursividad: ")
triangulorecursividad = triangulopascal2(filas)
print(triangulorecursividad)
#Imprime los dos triangulos de manera grafica
print("Representacion grafica del triangulo de pascal realizado por iteracion: ")
imprimirtriangulopascal(trianguloiteracion)
print("Representacion grafica del triangulo de pascal realizado por recursividad: ")
imprimirtriangulopascal(triangulorecursividad)

