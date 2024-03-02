


class Fraccion:
     def __init__(self,arriba,abajo):
          numer,denor=denNEG(arriba,abajo)
          if type(numer) == type(denor) == int:
               self.num = numer
               self.den = denor
          else:
               print("Tienen que ser números enteros")
          

     def __str__(self):
          return str(self.num)+"/" +str(self.den)

     def getNUM(self):
          return str(self.num)

     def getDEN(self):
          return str(self.den)

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

     def __ge__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den

          return primerNum >= segundoNum

     def __le__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den

          return primerNum <= segundoNum

     def __lt__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den

          return primerNum < segundoNum

     def __gt__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den

          return primerNum > segundoNum
            
     def __ne__(self, otro):
          primerNum = self.num * otro.den
          segundoNum = otro.num * self.den

          return primerNum != segundoNum



def mcd(m,n): #Esto no es un método, es una funcion
     while m%n != 0:
          mViejo = m
          nViejo = n
          m = nViejo
          n = mViejo%nViejo
     return n

def denNEG(n,d):
     while d<0:
          d=abs(d)
          n=-n
     return n,d




