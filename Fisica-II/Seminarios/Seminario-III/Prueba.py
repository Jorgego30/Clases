from rotaciones import *

angulo = float(input("Dime el angulo en grados: "))
angulo = np.radians(angulo)

x = float(input("Introduce la primera coordenada del vector eje: "))
y = float(input("Introduce la segunda coordenada del vector eje: "))
z = float(input("Introduce la tercera coordenada del vector eje: "))

eje = np.array([x,y,z])
eje = eje/np.linalg.norm(eje)
print(eje)

matriz = (rotacionRodrigues(eje,angulo))

print(f"\nLa matriz rotada es:\n{matriz}\n")

print(matrizLogaritmo(matriz))

