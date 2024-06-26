class Punto:
    @staticmethod #get_origen es un método estático
    def get_origen():
        return Punto(0,0)

    def calcula_distancia_origen(self):
        """Retorna la distancia desde el origen de coordenadas a este punto
            :return: La distancia entre ambos puntos
        """
        return self.calcula_distancia(Punto.get_origen())
