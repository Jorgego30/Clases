from Class_Fechas import *
from datetime import *
hoy=str(datetime.now()).split()
fecha2=hoy[0].split('-')
fecha1 = Fecha(int(fecha2[2]), int(fecha2[1]), int(fecha2[0]))

F = input('Dime el dia,mes,año o bien dia/mes/año: ').strip()

if F[-5] == ',': #se introduce fecha separada por comas
    Fech = F.replace(',', ' ')
    s = Fech.split()
    f = Fecha(int(s[0]), int(s[1]), int(s[2]))

    print('\nTu fecha: ', F)
    print('La fecha con la que comparamos: ', fecha1)
    print('Año Bisiesto?: ', f.bisiesto())
    print('Dia siguiente ', f.dia_siguiente())
    print('Es menor?: ',f.es_menor(fecha1))
    print('Es mayor?: ',f.__gt__(fecha1))
    print('Es igual?: ',f.__eq__(fecha1))
    print('Es mayor o igual?: ',f.__ge__(fecha1))
    print('Es menor o igual?: ',f.__le__(fecha1))



elif F[-5] == '/': #se introduce fecha separada por '/'
    Fech = F.replace('/', ' ')
    s = Fech.split()
    f = Fecha(int(s[0]), int(s[1]), int(s[2]))

    print('\nTu fecha: ', F)
    print('La fecha con la que comparamos: ', fecha1)
    print('Año Bisiesto?: ', f.bisiesto())
    print('Dia siguiente ', f.dia_siguiente())
    print('Es menor?: ',f.es_menor(fecha1))
    print('Es mayor?: ',f.__gt__(fecha1))
    print('Es igual?: ',f.__eq__(fecha1))
    print('Es mayor o igual?: ',f.__ge__(fecha1))
    print('Es menor o igual?: ',f.__le__(fecha1))
    
