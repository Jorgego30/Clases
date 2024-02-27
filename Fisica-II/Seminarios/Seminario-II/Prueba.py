from rotaciones import *

angulo = float(input("Dime el angulo en grados: "))
angulo = np.radians(angulo)

x = float(input("Introduce la primera coordenada del vector: "))
y = float(input("Introduce la segunda coordenada del vector: "))
z = float(input("Introduce la tercera coordenada del vector: "))

v = np.array([x,y,z])

eje = str(input("Dime el eje en el que quieres rotar el vector (x,y o z): ")).lower()

print(f"La rotacion del vector {v} respecto al eje {eje} es:\n{Rotv(eje,v,angulo)}")