#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - FUNCIONES - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def comparaciones(tipo, y):
    '''FUNCION QUE DEVUELVE LA CANTIDAD DE COMPARACIONES REALIZADAS EN UNA TABLA HASH MEDIANTE LA FORMULA DE DESEMPENHO'''
    '''
    tipo:
        1: exito en direccionamiento abierto
        2: fracaso en direccionamiento abierto
        3: exito en encadenamiento
        4: fracaso en encadenamiento
    y: porcentaje de llenado de la tabla hash
    '''
    if tipo == 1:
        return (0.5*(1+(1/(1-y))))
    elif tipo == 2:
        return (0.5*(1+pow((1/(1-y)),2)))
    elif tipo == 3:
        return (1+(y/2))
    elif tipo == 4:
        return y

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PROGRAMA PRINCIPAL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("Comparaciones promedio de una tabla hash: ")
print("                ----------------------- Exito --------------------      ------------------------------------- Fracaso ---------------------------")
print("Porcentaje       Direccionamiento Abierto           Encadenamiento      Direccionamiento Abierto                                 Encadenamiento")
for a in [0.1, 0.25, 0.5, 0.75, 0.9, 0.99]:
    print(f"{a:10} {round(comparaciones(1, a),2):20} {round(comparaciones(3, a), 2):28} {round(comparaciones(2, a),2):30} {round(comparaciones(4, a),2):50}")
print()
print("Se puede apreciar que a partir del 50%, la cantidad de comparaciones aumenta drasticamente, por lo que se podria decir que comienza a notarse la falta de tamanho de la misma. El caso de fracaso de direccionamiento abierto seria el que mas comparaciones realizaria. ")