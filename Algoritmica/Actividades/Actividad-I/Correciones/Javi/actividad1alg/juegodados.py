'''actividad 9: En un juego de dados, todos los participantes tienen el mismo número de dados (con n caras, de la 1 a la n).
En cada turno, cada jugador tira todos sus dados, sumando cada dado para obtener una puntuación. Gana el
jugador con mejor puntuación tras x turnos.'''


import random

class Jugador:
    def __init__(self, nombre, numero_dados, caras_dados):
        self.nombre = nombre
        self.numero_dados = numero_dados
        self.caras_dados = caras_dados

    def tirar_dados(self):
        # Simula el lanzamiento de todos los dados del jugador y devuelve la puntuación total
        return sum(random.randint(1, self.caras_dados) for _ in range(self.numero_dados))

class JuegoDados:
    def __init__(self, jugadores, numero_turnos):
        self.jugadores = jugadores
        self.numero_turnos = numero_turnos

    def jugar(self):
        # Simula el juego durante el número de turnos especificado
        resultados = {}

        for turno in range(1, self.numero_turnos + 1):
            print(f"\nTurno {turno}:")
            for jugador in self.jugadores:
                puntuacion_turno = jugador.tirar_dados()
                print(f"{jugador.nombre} tiró los dados y obtuvo {puntuacion_turno} puntos.")
                
                # Actualizar resultados
                if jugador.nombre not in resultados:
                    resultados[jugador.nombre] = 0
                resultados[jugador.nombre] += puntuacion_turno

        # Determinar al ganador
        ganador = max(resultados, key=resultados.get)
        print(f"\n¡{ganador} es el ganador con {resultados[ganador]} puntos!")

# Ejemplo de uso de las clases
jugador1 = Jugador("Jugador 1", numero_dados=2, caras_dados=6)
jugador2 = Jugador("Jugador 2", numero_dados=2, caras_dados=6)

juego = JuegoDados(jugadores=[jugador1, jugador2], numero_turnos=3)
juego.jugar()
