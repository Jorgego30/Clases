def sumalista(listaNumeros):
    if listaNumeros is None or not isinstance(listaNumeros,list):
        return None
    if len(listaNumeros) == 0:
        return 0
    else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])


print(sumalista([1,3,5,7,9]))