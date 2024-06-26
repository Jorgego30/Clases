def anagramaSolucion4(cadena1,cadena2):
    if len(cadena1)!=len(cadena2):
        return False
    
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(cadena1)):
        pos = ord(cadena1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(cadena2)):
        pos = ord(cadena2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    aunOK = True
    while j<26 and aunOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            aunOK = False

    return aunOK

print(anagramaSolucion4('cero','ocre'))
