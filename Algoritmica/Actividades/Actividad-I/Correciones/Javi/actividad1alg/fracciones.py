'''actividad3:Modifique el constructor para la clase Fracción de modo que compruebe que el numerador y el
denominador sean ambos enteros. Si alguno no es un entero, el constructor debe generar una excepción.
Implemente los métodos simples getNum y getDen eso devolverá el numerador y el denominador de una
fracción. Implementar los operadores relacionales restantes ( >, >=, <, <=, y !=)'''
class Fraccion:
    def __init__(self, arriba, abajo):
        # Comprobar que tanto el numerador como el denominador son enteros
        if not isinstance(arriba, int) or not isinstance(abajo, int):
            raise ValueError("Tanto el numerador como el denominador deben ser enteros.")
        
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
