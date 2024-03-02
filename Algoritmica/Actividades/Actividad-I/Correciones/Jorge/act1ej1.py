#Ejercicio1
from ClasePuertasAct1 import *

#Programa principal
def main():
    try:
        c1 = PuertaNAND("C1")
        c2 = PuertaNAND("C2")
        c3 = PuertaNOR("C3")
        c1 = Conector(c1, c3)
        c2 = Conector(c2, c3)
        
        print(c3.obtenerSalida())
        C1 = PuertaAND("C1")
        C2 = PuertaAND("C2")
        C3 = PuertaNOR("C3")
        C1 = Conector(C1, C3)
        C2 = Conector(C2, C3)
        print(C3.obtenerSalida())
        C11 = PuertaXOR("C1")
        C21 = PuertaXOR("C2")
        C31 = PuertaAND("C3")
        C11 = Conector(C11,C31)
        C21 = Conector(C21,C31)
        print(C31.obtenerSalida())
        C11 = PuertaNOR("C1")
        C21 = PuertaNOR("C2")
        C31 = PuertaXOR("C3")
        C11 = Conector(C11,C31)
        C21 = Conector(C21,C31)
        print(C31.obtenerSalida())
    except ValueError:
        print('Ha ocurrido un error inesperado')
    


main()