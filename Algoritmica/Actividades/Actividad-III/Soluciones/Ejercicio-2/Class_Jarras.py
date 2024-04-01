class Jarra:
    def __init__(self,capacidad):
        self.capacidad = capacidad
    
    def __str__(self):
        return str(self.capacidad)
    
    def transpose(self,otherJar,litrosApasar):
        if (self.capacidad<otherJar.capacidad):
            print (f"La primera jarra debe tener una mayor capacidad que la segunda")
            exit()

        litrosEnJarra1 = 0
        litrosEnJarra2 = 0

        print(f"Ambas jarras estan vacias")

        litrosEnJarra1 = self.capacidad
        print(f"Se llena la jarra de {self.capacidad}, ahora tiene {litrosEnJarra1}")
        while litrosEnJarra1 != litrosApasar:
            litrosEnJarra2 += litrosEnJarra1
            if (litrosEnJarra2 > otherJar.capacidad):
                litrosEnJarra1 = litrosEnJarra2 - otherJar.capacidad
                litrosEnJarra2 = 0

            print(f"Se llena la jarra de {otherJar.capacidad} con el liquido que estuviese en la otra jarra, ahora esta segunda jarra tiene {litrosEnJarra2} mientras que la primera tiene {litrosEnJarra1}")

            
