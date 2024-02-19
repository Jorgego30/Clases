import math

class Punto:
    # Crea una clase llamada Punto con sus dos coordenadas X e Y.
    def __init__(self, x=0, y=0):
        # Añade un método constructor para crear puntos fácilmente. 
        # Si no se recibe una de sus coordenadas, su valor será cero.
        self.x = x
        self.y = y

    def __str__(self):
        # Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca 
        # en formato (X,Y)
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        # Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, 
        # teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 
        # se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
        if self.x > 0 and self.y > 0:
            print(f"{self} pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(f"{self} pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(f"{self} pertenece al tercer cuadrante")
        elif self.x > 0 and self.y < 0:
            print(f"{self} pertenece al cuarto cuadrante")
        elif self.x != 0 and self.y == 0:
            print(f"{self} se sitúa sobre el eje X")
        elif self.x == 0 and self.y != 0:
            print(f"{self} se sitúa sobre el eje Y")
        else:
            print(f"{self} se encuentra sobre el origen")

#Otra forma de implementar el método cuadrante
    def cuadrante2(self):
        # Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, 
        # teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 
        # se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
        if self.x * self.y > 0:
            if self.x > 0 and self.y > 0:
                print(f"{self} pertenece al primer cuadrante")
            else:
                print(f"{self} pertenece al tercer cuadrante")
        elif self.x * self.y < 0:
                if self.x < 0 and self.y > 0:
                    print(f"{self} pertenece al segundo cuadrante")
                else:
                    print(f"{self} pertenece al cuarto cuadrante")
        elif self.x != 0 and self.y == 0:
            print(f"{self} se sitúa sobre el eje X")
        elif self.x == 0 and self.y != 0:
            print(f"{self} se sitúa sobre el eje Y")
        else:
            print(f"{self} se encuentra sobre el origen")

    def vector(self, p):
        # Añade un método llamado vector, que tome otro punto y calcule el vector resultante 
        # entre los dos puntos.
        print(f"El vector entre {self} y {p} es ({p.x - self.x}, {p.y - self.y})")
    
    def distancia(self, p):
        # Añade un método llamado distancia, que tome otro punto y calcule la distancia entre 
        # los dos puntos y la muestre por pantalla.
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es {d}")


class Rectangulo:
    # Crea una clase llamada Rectángulo con dos puntos (inicial y final) que formarán la 
    # diagonal del rectángulo.
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        # Añade un método constructor para crear ambos puntos fácilmente, si no se envían 
        # se crearán dos puntos en el origen por defecto.
        self.pInicial = pInicial
        self.pFinal = pFinal
        # Hago los cálculos, pero no denomino a los atributos igual
        # que los métodos porque sino podríamos sobreescribirlos
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        # Añade al rectángulo un método llamado base que muestre la base.
        print(f"La base del rectángulo es {self.vBase}")

    def altura(self):
        # Añade al rectángulo un método llamado altura que muestre la altura.
        print(f"La altura del rectángulo es {self.vAltura}")

    def area(self):
        # Añade al rectángulo un método llamado área que muestre el área.
        print(f"El área del rectángulo es {self.vArea}")
