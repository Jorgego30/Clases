from numpy.polynomial import Polynomial as P
class polinomios:

       
    def __init__(self, *coeficientes):
        """ input: coefficients are in the form a_n, ...a_1, a_0 
        """
        self.coeficientes = list(coeficientes) # tuple is turned into a list
     
    
    def __str__(self):
        """
        method to return the canonical string representation 
        of a polynomial.
        """
        return "El pololinomio es: " + str(P(self.coeficientes))
    
    def suma(self,otro):
        p1=P(self.coeficientes)
        p2=P(otro.coeficientes)
        print("La suma es: "+str(p1+p2))
    
    def resta(self,otro):
        p1=P(self.coeficientes)
        p2=P(otro.coeficientes)
        print("La resta es: "+str(p1-p2)) 
    
    def multiplicacion(self,otro):
        p1=P(self.coeficientes)
        p2=P(otro.coeficientes)
        print("La multiplicacion es: "+str(p1*p2)) 
    
    def division(self,otro):
        p1=P(self.coeficientes)
        p2=P(otro.coeficientes)
        resto= p1%p2
        print("La division es: "+str(p1//p2)+" El resto es: ",str(resto)) 
    
    def elevacion(self,elevado):
       p=P(self.coeficientes)
       print("El polinomio elevado a", elevado, "es: "+str(p**int(elevado)))