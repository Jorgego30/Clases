import numpy as np

class Polinomio:
    def __init__(self, coeficientes):
        self.polinomio = coeficientes
    
    def __str__(self):
        return f"{np.poly1d(self.polinomio)}"
    
    def __add__(self,otherPolinomio):
        suma = np.poly1d(self.polinomio) + np.poly1d(otherPolinomio.polinomio)
        return f"{suma}"
    
    def __sub__(self,otherPolinomio):
        resta = np.poly1d(self.polinomio) - np.poly1d(otherPolinomio.polinomio)
        return f"{resta}"
    
    def __mul__(self,otherPolinomio):
        multiplicacion = np.poly1d(self.polinomio) * np.poly1d(otherPolinomio.polinomio)
        return f"{multiplicacion}"
    
    def __truediv__(self,otherPolinomio):
        division = np.poly1d(self.polinomio) / np.poly1d(otherPolinomio.polinomio)
        return f"{division}"
