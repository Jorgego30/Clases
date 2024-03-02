 
from random import *
from Class_dados import *
 
if __name__ == "__main__":
    try:
        nturnos = int(input('Dame el turnos: '))
        ndados = int(input('Dame el numero de dados: '))
        while nturnos <=0 or ndados <=0:
            print('No puedes dar valores iguales o inferiores al 0')
            nturnos = int(input('Dame el turnos: '))
            ndados = int(input('Dame el numero de dados: '))
        juego = Juego(nturnos, ndados)
        juego.inserta_jugador("Sol")
        juego.inserta_jugador("Ky")
        juego.juega()
        print(juego)
    
    except ValueError:
        print('ha ocurrido un error inesperado')