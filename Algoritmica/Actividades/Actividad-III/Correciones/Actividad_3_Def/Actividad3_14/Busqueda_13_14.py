#Definimos una función que utiliza la busqueda secuencial no óptima. Es decir, que busca hasta el final o hasta que lo encuentra
def Busq_Secuencial_NoOpt(lista_no_ordenada,valor):
    pos = 0
    encontrado = False
    #Recorremos la lista buscando el elemento hasta que lleguemos al final o lo encontremos:
    while pos < len(lista_no_ordenada) and not encontrado:
        if lista_no_ordenada[pos] == valor:
            encontrado = True
        else:
            pos = pos+1
    #Devolvemos si encontramos el resultado o no
    return encontrado

#Definimos una función que utiliza la busqueda secuencial óptima. Es decir, que si el valor en la posición en la que estoy es mayor que el que busco deja de buscar porque está ordenada
def Busq_Secuencial_Opt(lista,valor):
    pos = 0
    encontrado = False
    parar = False
    #Recorremos la lista buscando el elemento hasta que lleguemos al final, lo encontremos o encontremos
    # un elemento mayor por lo que paramos ya que la lista está ordenada y no va a estar más adelante:
    while pos < len(lista) and not encontrado and not parar:
        if lista[pos] == valor:
            encontrado = True
        else:
            if lista[pos]>valor:
                parar = True
            else:
                pos = pos+1
    #Devolvemos si encontramos el resultado o no
    return encontrado

#Función de búsqueda binaria no recursiva:
def Busq_Binaria_Opt(lista,valor):
    primero = 0
    ultimo = len(lista)-1
    encontrado = False
    #Nos quedamos en este bucle hasta que se encuentre el valor o se llegue al final sin encontrarlo
    while primero<=ultimo and not encontrado:
        puntoMedio = (primero + ultimo)//2
        if lista[puntoMedio] == valor:
            encontrado = True
        else:
            if valor < lista[puntoMedio]:
                ultimo = puntoMedio-1
            else:
                primero = puntoMedio+1
    return encontrado

#Método de búsqueda binaria recursiva utilizando el operador corte:
def Busq_Binaria_Rec_Opt_corte(lista, valor):
    #Si llegamos a una lista de tamaño 0 y el valor no está en ella devolvemos False porq no se encontró
    if len(lista) == 0:
        return False
    else:
        puntoMedio = len(lista)//2
        if lista[puntoMedio] == valor:
            return True
        else:
            #Llamadas recursivas
            if valor < lista[puntoMedio]:
                return Busq_Binaria_Rec_Opt_corte(lista[:puntoMedio], valor)
            else:
                return Busq_Binaria_Rec_Opt_corte(lista[puntoMedio+1:], valor)

#Método de búsqueda binaria recursiva sin operador corte (alterando los límites entre los que buscar):
def Busq_Binaria_Rec_Opt(lista,valor,izq,der):
    #Si llegamos a una lista de tamaño 0 y el valor no está en ella devolvemos False porq no se encontró
    if izq==der:
        return False
    else:
        puntoMedio = (der+izq)//2
        if lista[puntoMedio] == valor:
            return True
        else:
            #Llamadas recursivas
            if valor < lista[puntoMedio]:
                return Busq_Binaria_Rec_Opt(lista, valor,izq,puntoMedio)
            else:
                return Busq_Binaria_Rec_Opt(lista, valor,puntoMedio+1,der)
