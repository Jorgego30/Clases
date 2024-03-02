from math import sqrt
class complejos:
    def __init__(self,num1,num2):
        self.real=num1
        self.imaginario=num2

    def __str__(self):
        if self.imaginario<0:
            return str(self.real)+" - " +str(abs(self.imaginario))+"i"
        else:
            return str(self.real)+" + " +str(self.imaginario)+"i"

    def __add__(self,otrocomplejo):
        nuevoreal = self.real + otrocomplejo.real
        nuevoimaginario = self.imaginario + otrocomplejo.imaginario
        return complejos(nuevoreal,nuevoimaginario)
    
    def __sub__(self,otrocomplejo):
        nuevoreal = self.real - otrocomplejo.real
        nuevoimaginario = self.imaginario - otrocomplejo.imaginario
        return complejos(nuevoreal,nuevoimaginario)

    def __mul__(self,otrocomplejo):
        nuevoreal = self.real*otrocomplejo.real-self.imaginario*otrocomplejo.imaginario
        nuevoimaginario = self.imaginario*otrocomplejo.real + self.real*otrocomplejo.imaginario
        return complejos(nuevoreal,nuevoimaginario)
    
    
    def módulo(self):
        modulo=sqrt(self.real**2+self.imaginario**2)
        return modulo
     
    def __truediv__(self,otrocomplejo):
        nuevoreal = (self.real*otrocomplejo.real-(-self.imaginario)*otrocomplejo.imaginario)/(otrocomplejo.real**2+otrocomplejo.imaginario**2)
        nuevoimaginario = (self.imaginario*otrocomplejo.real - self.real*otrocomplejo.imaginario)/(otrocomplejo.real**2+otrocomplejo.imaginario**2)
        
        return complejos(nuevoreal,nuevoimaginario)

    def __eq__(self, otro):
        if self.real==otro.real and self.imaginario==otro.imaginario:
            return True
        
        else:
            return False



    def __ne__(self, otro):
        if self.real!=otro.real or self.imaginario!=otro.imaginario:
            return True
        
        else:
            return False

    def __ge__(self,otro):
        if self.real>=otro.real and self.imaginario>=otro.imaginario:
            return True
        
        else:
            return False

    def __le__(self,otro):
        if self.real<=otro.real and self.imaginario<=otro.imaginario:
            return True
        
        else:
            return False

    def __gt__(self,otro):
        if self.real>otro.real and self.imaginario>otro.imaginario:
            return True
        
        else:
            return False
        



    
        