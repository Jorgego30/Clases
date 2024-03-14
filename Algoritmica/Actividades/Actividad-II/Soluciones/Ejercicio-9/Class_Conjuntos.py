class Conjunto:
    def __init__(self):
        self.elementos=[]


    def inserta(self,elemento):
        if not (elemento in self.elementos):
            self.elementos.append(elemento)
    
    
    def __str__(self):
        cadena='{'
        if len(self.elementos)>0:
            for elemento in self.elementos[:-1]:
                cadena=cadena+str(elemento)+', '
            cadena=cadena+str(self.elementos[-1])
        return cadena+'}'
    
    
    def tamaño(self):
        return len(self.elementos)
    
    
    def pertenece(self, elemento):
        return elemento in self.elementos
    
    def elimina(self, elemento):
        if (self.pertenece(elemento)):
            self.elementos.remove(elemento)
        else:
            print (f"El elemento que quieres eliminar no esta en el conjunto")

    def union(self, otherConjunto):
        union = Conjunto()
        for i in self.elementos:
            union.inserta(i)
        for i in otherConjunto.elementos:
            union.inserta(i)
        return union
    
    def interseccion(self, otherConjunto):
        interseccion = Conjunto()
        for i in self.elementos:
            if (i in otherConjunto.elementos):
                interseccion.inserta(i)
        return interseccion
    
    def diferencia(self, otherConjunto):
        diferencia = Conjunto()
        for i in self.elementos:
            diferencia.inserta(i)
        for i in otherConjunto.elementos:
            diferencia.inserta(i)
        
        interseccion = Conjunto()
        for i in self.elementos:
            if (i in otherConjunto.elementos):
                interseccion.inserta(i)
        
        for i in interseccion.elementos:
            if (i in diferencia.elementos):
                diferencia.elimina(i)
        return diferencia
    
    def incluye(self,otherConjunto):
        bool = True
        for i in self.elementos:
            if (i not in otherConjunto.elementos):
                bool = False
        
        if bool == True:
            return f"El conjunto {self.elementos} pertenece al conjunto {otherConjunto.elementos}"
        elif bool == False:
            return f"El conjunto {self.elementos} no pertenece al conjunto {otherConjunto.elementos}"
