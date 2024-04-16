'''Actividad 8:


Generaliza el programa 2 de esta actividad:
Tienes dos jarras, una de X litros y otra de Y litros, con X>Y. Ninguna de las jarras tiene marcas en ella.
Hay una bomba que se puede utilizar para llenar las jarras con agua. ¿Cómo se pueden obtener
exactamente X/2 litros de agua en la jarra de X litros?
'''

from Class_Jarra import *

capacidad_x = 8 #Modificar los valores con cuidado ya que hay ciertas combinaciones que pueden necesitar muchos recursos
capacidad_y = 2
jarras = Jarras(capacidad_x, capacidad_y)
print("Cantidad de agua en la jarra de X después de obtener X/2 litros:", jarras.obtener_x_medio())