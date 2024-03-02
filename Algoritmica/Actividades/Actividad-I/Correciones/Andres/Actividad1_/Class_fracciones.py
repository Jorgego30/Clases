#Class_Fracciones.py
class Fraccion:

    def _init_(self,arriba,abajo):

            if type(arriba)!=type(abajo)!=int:
                raise Exception('Fallo, el numerador y el denominador deben ser el mismo.')
            else:
                if abajo<0:
                    self.den = abs(abajo)
                    self.num = arriba * -1
                else:
                    self.num = arriba
                    self.den = abajo

    def __str__(self):
        return str(self.num)+"/" +str(self.den)
    
    def __add__(self,otraFraccion):

        nuevoNum = self.num*otraFraccion.den + self.den*otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum,nuevoDen)
        return Fraccion(nuevoNum//comun,nuevoDen//comun)
    
    def __sub__(self,otraFraccion):

        nuevoNum = self.num*otraFraccion.den - self.den*otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum,nuevoDen)
        return Fraccion(nuevoNum//comun,nuevoDen//comun)
    
    def __mul__(self,otraFraccion):

        nuevoNum = self.num*otraFraccion.num
        nuevoDen = self.den * otraFraccion.den
        comun = mcd(nuevoNum,nuevoDen)
        return Fraccion(nuevoNum//comun,nuevoDen//comun)
    
    def __truediv__(self,otraFraccion):

        nuevoNum = self.num*otraFraccion.den
        nuevoDen = self.den * otraFraccion.num
        comun = mcd(nuevoNum,nuevoDen)
        return Fraccion(nuevoNum//comun,nuevoDen//comun)
    
    def __eq__(self, otro):

        primerNum = self.num * otro.den
        segundoNum = otro.num * self.den
        return primerNum == segundoNum
    
def mcd(m,n):
    while m%n != 0:
        mViejo = m
        nViejo = n
        m = nViejo
        n = mViejo%nViejo
        return n
    
def getNum(self):
    print