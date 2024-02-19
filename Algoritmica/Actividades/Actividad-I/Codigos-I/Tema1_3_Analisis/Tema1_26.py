def anagramaSolucion3(cadena1,cadena2):
    if len(cadena1)!=len(cadena2):
        return False

    unaLista1 = list(cadena1)
    unaLista2 = list(cadena2)

    unaLista1.sort()
    unaLista2.sort()

    pos = 0
    coincide = True

    while pos < len(cadena1) and coincide:
        if unaLista1[pos]==unaLista2[pos]:
            pos = pos + 1
        else:
            coincide = False

    return coincide

print(anagramaSolucion3('abcde','edcba'))


