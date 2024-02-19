class Complejo:
    def __init__(self,parteReal, parteImaginaria):
        
        self.parteReal = parteReal
        self.parteImaginaria = parteImaginaria
        self.complejo = complex(parteReal,parteImaginaria)
        
    def __str__ (self):
        return f"{self.complejo}"

    def __lt__ (self, otherComplex):
        return self.parteReal < otherComplex.parteReal and self.parteImaginaria < otherComplex.parteImaginaria
    
    def __le__ (self, otherComplex):
        return self.parteReal <= otherComplex.parteReal and self.parteImaginaria <= otherComplex.parteImaginaria
    
    def __gt__ (self, otherComplex):
        return self.parteReal > otherComplex.parteReal and self.parteImaginaria > otherComplex.parteImaginaria
    
    def __ge__ (self, otherComplex):
        return self.parteReal >= otherComplex.parteReal and self.parteImaginaria >= otherComplex.parteImaginaria
    
    def __eq__ (self, otherComplex):
        return self.parteReal == otherComplex.parteReal and self.parteImaginaria == otherComplex.parteImaginaria
    
    def __add__(self,otherComplex):
        newRealPart = self.parteReal + otherComplex.parteReal
        newImaginaryPart = self.parteImaginaria + otherComplex.parteImaginaria
        return complex(newRealPart,newImaginaryPart)
    
    def __sub__(self,otherComplex):
        newRealPart = self.parteReal - otherComplex.parteReal
        newImaginaryPart = self.parteImaginaria - otherComplex.parteImaginaria
        return complex(newRealPart,newImaginaryPart)
    
    def __mul__(self,otherComplex):
        newRealPart = self.parteReal * otherComplex.parteReal + ((self.parteImaginaria * otherComplex.parteImaginaria)*-1)
        newImaginaryPart = self.parteReal * otherComplex.parteImaginaria + self.parteImaginaria * otherComplex.parteReal
        return complex(newRealPart,newImaginaryPart)
    
    def __truediv__(self,otherComplex):
        complejo1 = complex(self.parteReal,self.parteImaginaria)
        complejo2 = complex(otherComplex.parteReal,otherComplex.parteImaginaria)
        return complejo1/complejo2
    
    def valor_absoluto(self):
        return abs(complex(self.parteReal,self.parteImaginaria))
    
    def conjugado(self):
        return complex(self.parteReal, -self.parteImaginaria)
    
    def getReal(self):
        return f"{self.parteReal}"
    
    def getImaginary(self):
        return f"{self.parteImaginaria}"