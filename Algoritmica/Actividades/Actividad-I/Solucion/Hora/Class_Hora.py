def validacion(hora,minutos,segundos):
    if(type(hora) != int):
        print(f"La hora debe ser un entero")
        return False
    elif(type(minutos) != int):
        print(f"Los minutos debe ser un entero")
        return False
    elif(type(segundos) != int):
        print(f"Los segundos debe ser un entero")
        return False
    else:
        return True
    

def comprobacion(hora,minutos,segundos):
    if validacion(hora,minutos,segundos)==True:
        if (hora <0 or hora>23):
            print(f"La hora {hora} es invalida ya que no esta dentro de las 24 horas del dia")
            return False
        elif (minutos<0 or minutos>59):
            print(f"Los minutos {minutos} es invalida ya que no esta dentro de los 59 minutos de una hora")
            return False
        elif (segundos<0 or segundos>59):
            print(f"Los segundos {segundos} es invalida ya que no esta dentro de los 59 segundos de un minuto")
            return False
        else:
            return True
    else:
        return False

class Hora:
    def __init__(self,hora,minutos,segundos):
        if (comprobacion(hora,minutos, segundos)==True):
            self.hora = hora
            self.minutos = minutos
            self.segundos = segundos
        else:
            print("La hora es invalida")

    def __str__ (self):
        return f"La hora es: {self.hora}:{self.minutos}:{self.segundos}"
    
    def es_menor(self,hora1):
        if self.hora<hora1.hora:
            return True
        elif self.hora>hora1.hora:
            return False
        if self.minutos<hora1.minutos:
            return True
        elif self.minutos>hora1.minutos:
            return False
        return self.segundos<hora1.segundos
    
    def es_mayor(self,hora1):
        if self.hora<hora1.hora:
            return False
        elif self.hora>hora1.hora:
            return True
        if self.minutos<hora1.minutos:
            return False
        elif self.minutos>hora1.minutos:
            return True
        return self.segundos>hora1.segundos
    
    def es_igual(self,hora1):
        if self.hora==hora1.hora:
            return True
        elif self.hora!=hora1.hora:
            return False
        if self.minutos==hora1.minutos:
            return True
        elif self.minutos!=hora1.minutos:
            return False
        return self.segundos==hora1.segundos
    
    def __add__ (self,otherHour):
        newHour = self.hora + otherHour.hora
        newMin = self.minutos + otherHour.minutos
        newSec = self.segundos + otherHour.segundos

        if(newHour>23):
            newHour-=23
        
        if(newMin>59):
            newMin -= 59
            newHour += 1
            if(newHour>23):
                newHour-=23

        if (newSec>59):
            newSec -= 59
            newMin += 1
            if(newMin>59):
                newMin -= 59
                newHour += 1
                if(newHour>23):
                    newHour-=23
        return f"La hora es: {newHour}:{newMin}:{newSec}"
        
    def __sub__ (self,otherHour):
        newHour = self.hora - otherHour.hora
        newMin = self.minutos - otherHour.minutos
        newSec = self.segundos - otherHour.segundos

        if(newHour<0):
            newHour += 23
        
        if(newMin<0):
            newMin += 59
            newHour -= 1
            if(newHour<0):
                newHour += 23

        if (newSec<0):
            newSec += 59
            newMin -= 1
            if(newMin<0):
                newMin += 59
                newHour -= 1
                if(newHour<0):
                    newHour += 23

        return f"La hora es: {newHour}:{newMin}:{newSec}"
        
    def getSegundosTotales (self):
        totalSec = self.hora*3600 + self.minutos*60 + self.segundos

        return totalSec