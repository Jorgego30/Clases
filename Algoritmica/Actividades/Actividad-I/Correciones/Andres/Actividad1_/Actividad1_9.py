from Class_Juego_Dados import *

try:
    random.seed()
    juego = Juego(3, 5)
    juego.inserta_jugador("Roberto carlos")
    juego.inserta_jugador("Fulano")
    juego.inserta_jugador("Mengano")
    juego.inserta_jugador("Zutano")
    juego.juega()
    print(juego)
except(ValueError):
    print("Se ha producido un error en la ejecucion del programa, revisa que has introducido todos los datos correctamente.\n")