from Class_Juego import *

random.seed()
juego = Juego(random.randint(2, 6), random.randint(3, 6), random.randint(4,20))
juego.inserta_jugador("Baltasar")
juego.inserta_jugador("Fulano")
juego.inserta_jugador("Mengano")
juego.inserta_jugador("Zutano")
juego.juega()
print(juego)

