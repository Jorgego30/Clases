def validacion(dia,mes,año):
    if(type(dia) != int):
        print(f"El dia debe ser un entero")
        return False
    elif(type(mes) != int):
        print(f"El mes debe ser un entero")
        return False
    elif (type(año) != int):
        print(f"El año debe ser un entero")
        return False
    else:
        return True

def bisies(año):
    return año%4==0 and (año%100!=0 or año%400==0)

def fechaCorrecta(dia,mes,año):

    if validacion(dia,mes,año) == True:
        global masDias 
        masDias = [1,3,5,7,8,10,12]
        global menosDias 
        menosDias = [4,6,9,11]
        
        if dia<1:
            print(f"El dia {dia} es invalido ya que para cualquier mes el minimo de dias es 1")
            return False
        elif mes <1 or mes>12:
            print(f"El mes {mes} es invalido ya que no se encuentra entre los 12 meses del año")
            return False
        elif mes in masDias:
            if dia > 31:
                print(f"El dia {dia} es invalido ya que para el mes {mes} el maximo de dias es 31")
                return False
            else:
                return True
        elif mes in menosDias:
            if dia > 30:
                print(f"El dia {dia} es invalido ya que para el mes {mes} el maximo de dias es 31")
                return False
            else:
                return True
        elif mes == 2:
            if bisies(año) == True and dia > 29:
                print(f"El dia {dia} es invalido ya que en el año {año} febrero es bisiesto por lo que el maximo de dias es 29")
                return False
            elif bisies(año) == False and dia > 28:
                print(f"El dia {dia} es invalido ya que en el año {año} febrero no es bisiesto por lo que el maximo de dias es 28")
                return False
            else:
                return True
        else:
            return True
    else:
        return False

class Fecha:
    def __init__(self,dia,mes,año):
        
        if (fechaCorrecta(dia,mes,año)==True):
            self.dia=dia
            self.mes=mes
            self.año=año
        else:
            print("La fecha que has proporcionado es erronea")

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
        if self.año<fecha1.año:
            return False
        elif self.año>fecha1.año:
            return True
        if self.mes<fecha1.mes:
            return False
        elif self.mes>fecha1.mes:
            return True
        return self.dia>fecha1.dia
    
    def es_igual(self,fecha1):
        if self.año==fecha1.año:
            return True
        elif self.año!=fecha1.año:
            return False
        if self.mes==fecha1.mes:
            return True
        elif self.mes!=fecha1.mes:
            return False
        return self.dia==fecha1.dia
    
    def __add__ (self,otherDay):
        newDay = self.dia + otherDay.dia
        newMonth = self.mes + otherDay.mes
        newYear = self.año + otherDay.año

        if (newMonth>12):
            newMonth -= 12
            newYear += 1

        if(newMonth<13 and newMonth in masDias):
            if (newDay>31):
                newDay -= 31
                if (newMonth>12):
                    newMonth -= 12
                    newYear += 1
        elif(newMonth<13 and newMonth in menosDias):
            if (newDay>30):
                newDay -= 30
                if (newMonth>12):
                    newMonth -= 12
                    newYear += 1
        elif(newMonth == 2 and bisies(newYear) == True):
            if(newDay>29):
                newDay -= 29
        elif(newMonth == 2 and bisies(newYear) == False):
            if(newDay>28):
                newDay -= 28    

        return f'{newDay}/{newMonth}/{newYear}'
     
    def __sub__ (self,otherDay):
        newDay = self.dia - otherDay.dia
        newMonth = self.mes - otherDay.mes        
        newYear = self.año - otherDay.año
        
        if (newMonth<1):
            newMonth += 12
            newYear -= 1

        if(newMonth>0 and newMonth in masDias):
            if (newDay<1):
                newDay += 31
                if (newMonth<1):
                    newMonth += 12
                    newYear -= 1
        elif(newMonth>0 and newMonth in menosDias):
            if (newDay<1):
                newDay += 30
                if (newMonth<1):
                    newMonth += 12
                    newYear -= 1
        elif(newMonth == 2 and bisies(newYear) == True):
            if(newDay<29):
                newDay += 29
        elif(newMonth == 2 and bisies(newYear) == False):
            if(newDay<28):
                newDay += 28    

        return f'{newDay}/{newMonth}/{newYear}'