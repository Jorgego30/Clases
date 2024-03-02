'''actividad 9: En un juego de dados, todos los participantes tienen el mismo número de dados (con n caras, de la 1 a la n).
En cada turno, cada jugador tira todos sus dados, sumando cada dado para obtener una puntuación. Gana el
jugador con mejor puntuación tras x turnos.'''

from juegodados import Jugador, JuegoDados

# Ejemplo de uso de las clases
jugador1 = Jugador("Jugador 1", numero_dados=2, caras_dados=6)
jugador2 = Jugador("Jugador 2", numero_dados=2, caras_dados=6)

juego = JuegoDados(jugadores=[jugador1, jugador2], numero_turnos=3)
juego.jugar()
