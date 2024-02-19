def anagramaSolucion1(cadena1,cadena2):
    if len(cadena1)!=len(cadena2):
        return False
    unaLista = list(cadena2)
    pos1 = 0
    aunOK = True

    while pos1 < len(cadena1) and aunOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(unaLista) and not encontrado:
            if cadena1[pos1] == unaLista[pos2]:
                encontrado = True
            else:
                pos2 = pos2 + 1

        if encontrado:
            unaLista[pos2] = None
        else:
            aunOK = False

        pos1 = pos1 + 1

    return aunOK

print(anagramaSolucion1('abcd','dcba'))
