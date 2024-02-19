from Class_Hora import *
from datetime import *

hoy = str(datetime.now()).split()
hour = hoy[1].split(':')
hora1 = Hora(int(hour[0]),int(hour[1]),int(hour[2].split('.')[0]))
print (hora1)

H = input('Dime el hora:minutos:segundos : ').strip()

if H.count(':') >= 1 : #se introduce fecha separada por comas
    Fech = H.replace(':', ' ')
    s = Fech.split()
    h = Hora(int(s[0]), int(s[1]), int(s[2]))

    print('\nTu hora: ', H)
    print('La hora con la que comparamos: ', hora1)
    print('Menor que la hora actual?: ', h.es_menor(hora1))
    print('Mayor que la hora actual?: ', h.es_mayor(hora1))
    print('Igual que la hora actual?: ', h.es_igual(hora1))

    addHour = h + hora1
    subHour = h - hora1

    print(f"La suma de la hora {h} y la hora {hora1} es: {addHour}")
    print(f"La resta de la hora {h} y la hora {hora1} es: {subHour}")

    print(f"El total de segundos de la hora {h} es: {h.getSegundosTotales()}")