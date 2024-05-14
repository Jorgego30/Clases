
# El algoritmo construirGrafo es de orden N al cubo, debido a que hay 3 for encapsulados uno dentro de otro



def construirGrafo(archivoPalabras):
    d = {}
    g = Grafo()
    archivo = open(archivoPalabras,'r')
    # crear recipientes de palabras que se diferencian por una letra
    for linea in archivo:
        palabra = linea[:-1]
        for i in range(len(palabra)):
            recipiente = palabra[:i] + '_' + palabra[i+1:]
            if recipiente in d:
                d[recipiente].append(palabra)
            else:
                d[recipiente] = [palabra]
    print(d)
    # agregar vértices y aristas para palabras en el mismo recipiente
    for recipiente in d.keys():
        for palabra1 in d[recipiente]:
            for palabra2 in d[recipiente]:
                if palabra1 != palabra2:
                    g.agregarArista(palabra1,palabra2)
    
