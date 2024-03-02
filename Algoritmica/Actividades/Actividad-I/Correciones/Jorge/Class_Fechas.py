class Fecha:
    def __init__(self,dia,mes,año):
        if type(dia) != int or dia < 1 or dia > 30:
            raise Exception("El día introducido debe ser un número entero entre [1-30]")
        self.dia=dia
        self.mes=mes
        self.año=año

    def __str__(self):
        if self.dia<30 or self.mes<12:
            return '{0}/{1}/{2}'.format(self.dia,self.mes,self.año)
        else:
            return 'Ha ocurrido un error al introducir el dia o la fecha'

    def bisiesto(self):
        if self.dia<30 or self.mes<12:
            return self.año%4==0 and (self.año%100!=0 or self.año%400==0)
        else:
            return 'Ha ocurrido un error al introducir el dia o la fecha'

    def es_menor(self,fecha1):
        if self.año<fecha1.año:
            return True
        elif self.año>fecha1.año:
            return False
        if self.mes<fecha1.mes:
            return True
        elif self.mes>fecha1.mes:
            return False
        return self.dia<fecha1.dia

    def dia_siguiente(self):
            
            self.dia = self.dia +1
        
            if self.dia == 31 :
                self.dia = 1
                self.mes = self.mes+1
                if self.mes == 13:
                    self.mes = 1
                    self.año = self.año +1
            return '{0}/{1}/{2}'.format(self.dia,self.mes,self.año)

    def __eq__(self,fecha1):
        if self.año==fecha1.año:
            return True
        elif self.año!=fecha1.año:
            return False
        if self.mes==fecha1.mes:
            return True
        elif self.mes!=fecha1.mes:
            return False
        return self.dia==fecha1.dia

    def __ge__(self,fecha1):
        if self.año>=fecha1.año:
            return True
        elif self.año<fecha1.año:
            return False
        if self.mes>=fecha1.mes:
            return True
        elif self.mes<fecha1.mes:
            return False
        return self.dia>=fecha1.dia

    def __le__(self,fecha1):
        if self.año<=fecha1.año:
            return True
        elif self.año>fecha1.año:
            return False
        if self.mes<=fecha1.mes:
            return True
        elif self.mes>fecha1.mes:
            return False
        return self.dia<=fecha1.dia

    def __gt__(self,fecha1):
        if self.año>fecha1.año:
            return True
        elif self.año<fecha1.año:
            return False
        if self.mes>fecha1.mes:
            return True
        elif self.mes<fecha1.mes:
            return False
        return self.dia>fecha1.dia

    def __ne__(self,fecha1):
        if self.año!=fecha1.año:
            return True
        elif self.año==fecha1.año:
            return False
        if self.mes!=fecha1.mes:
            return True
        elif self.mes==fecha1.mes:
            return False
        return self.dia!=fecha1.dia

    
    

    
            

    

    
    
