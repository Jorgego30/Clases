from Class_Estructuras_lineales import Pila

def infija_a_prefija(expresionInfija):
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia[")"] = 1  # Cambiamos la precedencia de '(' a ')' para ajustar el enfoque de prefija.
    precedencia["("] = 0
    pilaOperadores = Pila()
    listaPrefija = []
    listaSimbolos = expresionInfija.split()

    for simbolo in reversed(listaSimbolos):  # Invertimos la lista de símbolos de entrada.
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo in "0123456789":
            listaPrefija.append(simbolo)
        elif simbolo == ')':
            pilaOperadores.incluir(simbolo)
        elif simbolo == '(':
            simboloTope = pilaOperadores.extraer()
            while simboloTope != ')':
                listaPrefija.append(simboloTope)
                simboloTope = pilaOperadores.extraer()
        else:
            while (not pilaOperadores.estaVacia()) and (precedencia[pilaOperadores.inspeccionar()] > precedencia[simbolo]):
                listaPrefija.append(pilaOperadores.extraer())
            pilaOperadores.incluir(simbolo)

    while not pilaOperadores.estaVacia():
        listaPrefija.append(pilaOperadores.extraer())
    return " ".join(reversed(listaPrefija))  # Invertimos la lista de salida para obtener la expresión prefija.


def normaliza(expr):
    Nexpr = ""
    for c in expr:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or c in "*+/-" or c in "0123456789":
            Nexpr = Nexpr + c + ' '
    return Nexpr


print(infija_a_prefija(normaliza("(A2+ B)*(C+D)*(E+F)")))
print(infija_a_prefija(normaliza("A+((B+C)*(D+E))")))
print(infija_a_prefija(normaliza("A*B*C*D+E+F ")))
