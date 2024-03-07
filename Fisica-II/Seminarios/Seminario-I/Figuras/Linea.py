import numpy as np
import matplotlib.pyplot as plt

def create_line(center, dir_vector, length, steps):
	v = np.array(dir_vector)
	print (f"El vector director se convierte en: {v}")
	v = v / np.linalg.norm(v)
	print (f"El vector director se normaliza a: {v}")
	start = np.array(center) - length * 0.5 * v # punto inicial del segmento
	print(f"El inicio es: {start}\n")

	# El numero de steps define la resolucion del segmento
	points = np.zeros((steps+1, 3))
	print(f"Puntos en 0: {points}\n")
	# Generamos los puntos del segmento
	for i in range(steps+1):
		x = length / steps * i
		print(f"X es: {x}")
		points[i,:] = x * v + start
		print(f"Puntos:\n {points}\n")
		
	# Devolvemos el array que contiene los puntos del segmento
	return points
	
center=[0,0,0]
dir_vector=[1,1,0]
length=8
steps=10
line = create_line(center, dir_vector, length, steps)
#print(line)
plt.plot(line[:,0],line[:,1], linewidth=2.0, marker='o')
plt.show()
