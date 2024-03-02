class Fecha:
    def __init__(self,dia,mes,año):
        #Validamos la lectura del dato para que si no cumple los requisitos no se forme.
        if dia>30 or dia<0 or mes>12 or mes<0 or año>2024 or año<0:
            raise (ValueError("Error en la lectura del dato"))
        else:
            self.dia=dia
            self.mes=mes
            self.año=año

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.año}'

    def bisiesto(self):
        return self.año%4==0 and (self.año%100!=0 or self.año%400==0)

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
    def es_mayor(self,fecha1):
        if self.año>fecha1.año:
            return True
        elif self.año<fecha1.año:
            return False
        if self.mes>fecha1.mes:
            return True
        elif self.mes<fecha1.mes:
            return False
        return self.dia>fecha1.dia
    
