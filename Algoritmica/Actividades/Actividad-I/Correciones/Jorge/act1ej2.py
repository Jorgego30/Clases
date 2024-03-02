from Clase_logica import*

def main():
    A=[True,False]
    B=[True,False]
    C=[True,False]
    D=[True,False]
    F=[False,False,False,False,False,False,False,False]
    G=[True,True,True,True,True,True,True,True]

    ecuacion_final=ecuacion(A,B,C,D,F,G)
    print(ecuacion_final.comprobarEcuacion())

main()