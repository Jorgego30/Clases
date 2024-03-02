class horas:
    def __init__(self,hora,minuto,segundo):
         
        if (minuto and segundo)>60 or hora>24 or type(hora)!=int or type(minuto)!=int or type(segundo)!=int:
            print("Las horas no pueden ser mayores de 24 ni los minutos y segundos mayores de 60")
            exit()
        else:
            self.horas = hora
            self.minutos = minuto
            self.segundos = segundo

   
    def __str__(self):
          return str(self.horas)+":" +str(self.minutos) + ":" +str(self.segundos)
        
    def __add__(self,otrahora):
        nuevashoras=self.horas+otrahora.horas
        nuevosminutos=self.minutos+otrahora.minutos
        nuevossegundos=self.segundos+otrahora.segundos
        while nuevashoras>=24:
            nuevashoras=nuevashoras%24
        while nuevosminutos>=60:
            nuevosminutos=nuevosminutos%60
            nuevashoras=nuevashoras+1
        while nuevossegundos>=60:
            nuevossegundos=nuevossegundos%60
            nuevosminutos=nuevosminutos+1
        return horas(nuevashoras,nuevosminutos,nuevossegundos)
    
    def __sub__(self,otrahora):
        nuevashoras=self.horas-otrahora.horas
        nuevosminutos=self.minutos-otrahora.minutos
        nuevossegundos=self.segundos-otrahora.segundos
        if nuevossegundos<0:
            nuevosminutos=nuevosminutos-1
            nuevossegundos=nuevossegundos+60
        if nuevosminutos<0:
            nuevosminutos=nuevosminutos+60
            nuevashoras=nuevashoras-1
        if self.horas<otrahora.horas:
            print("No se puede restar porque las horas son mayores ")
            exit()
        return horas(nuevashoras,nuevosminutos,nuevossegundos)

    def pasarhora(self):
        if self.horas>12:
            self.horas=self.horas-12
        return(self.horas,self.minutos,self.segundos)

    def __eq__(self, otro):
            if self.horas==otro.horas and self.minutos==otro.minutos and self.segundos==otro.segundos:
                return True
            else:
                return False

    def __ge__(self, otro):
            if self.horas==otro.horas:
                if self.minutos==otro.minutos:
                    if self.segundos<otro.segundos:
                       return False
                    else:
                        return True
                elif self.minutos<otro.minutos:
                    return False
                else:
                    return True 
            elif self.horas<otro.horas:
                return False       
            else:
                return True

    def __le__(self, otro):
            if self.horas==otro.horas:
                if self.minutos==otro.minutos:
                    if self.segundos>otro.segundos:
                       return False
                    else:
                        return True
                elif self.minutos>otro.minutos:
                    return False
                else:
                    return True 
            elif self.horas>otro.horas:
                return False       
            else:
                return True

    def __lt__(self, otro):
            if self.horas==otro.horas:
                if self.minutos==otro.minutos:
                    if self.segundos>=otro.segundos:
                       return False
                    else:
                        return True
                elif self.minutos>otro.minutos:
                    return False
                else:
                    return True 
            elif self.horas>otro.horas:
                return False       
            else:
                return True

    def __gt__(self, otro):
            if self.horas==otro.horas:
                if self.minutos==otro.minutos:
                    if self.segundos<=otro.segundos:
                       return False
                    else:
                        return True
                elif self.minutos<otro.minutos:
                    return False
                else:
                    return True 
            elif self.horas<otro.horas:
                return False       
            else:
                return True
            
    def __ne__(self, otro):
        if self.horas==otro.horas and self.minutos==otro.minutos and self.segundos==otro.segundos:
                return False
        else:
                return True
