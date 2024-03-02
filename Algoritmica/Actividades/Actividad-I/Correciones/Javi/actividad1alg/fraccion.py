'''actividad4:En la definición de fracciones asumimos que las fracciones negativas tienen un numerador negativo y un
denominador positivo. El uso de un denominador negativo haría que algunos de los operadores relacionales
dieran resultados incorrectos. En general, ésta es una restricción innecesaria. Modifique el constructor para
permitir que el usuario pase un denominador negativo y que todos los operadores continúen funcionando
correctamente.'''
class Fraccion:
    def __init__(self, arriba, abajo):
        # Comprobar que el denominador sea un entero
        if not isinstance(arriba, int) or not isinstance(abajo, int):
            raise ValueError("Tanto el numerador como el denominador deben ser enteros.")
        
        # Asegurarse de que el denominador sea positivo
        if abajo < 0:
            arriba = -arriba
            abajo = -abajo

        self.num = arriba
        self.den = abajo

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otraFraccion):
        nuevoNum = self.num * otraFraccion.den + self.den * otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __sub__(self, otraFraccion):
        nuevoNum = self.num * otraFraccion.den - self.den * otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __mul__(self, otraFraccion):
        nuevoNum = self.num * otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __truediv__(self, otraFraccion):
        nuevoNum = self.num * otraFraccion.den
        nuevoDen = self.den * otraFraccion.num
        comun = mcd(nuevoNum, nuevoDen)
        return Fraccion(nuevoNum // comun, nuevoDen // comun)

    def __eq__(self, otro):
        primerNum = self.num * otro.den
        segundoNum = otro.num * self.den
        return primerNum == segundoNum

    def __ne__(self, otro):
        return not self.__eq__(otro)

    def __lt__(self, otro):
        primerNum = self.num * otro.den
        segundoNum = otro.num * self.den
        return primerNum < segundoNum

    def __le__(self, otro):
        return self.__lt__(otro) or self.__eq__(otro)

    def __gt__(self, otro):
        return not self.__le__(otro)

    def __ge__(self, otro):
        return not self.__lt__(otro)

def mcd(m, n):
    while m % n != 0:
        mViejo = m
        nViejo = n
        m = nViejo
        n = mViejo % nViejo
    return n

