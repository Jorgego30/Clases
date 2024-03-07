import numpy as np
import matplotlib.pyplot as plt


def create_paralelogram(center, v1, v2, l1, l2, steps):
	v1 = np.array(v1)
	v1 = v1 / np.linalg.norm(v1)
	print (f"La base es: {v1}")
	v2 = np.array(v2)
	v2 = v2 / np.linalg.norm(v2)
	print (f"La altura es: {v2}")	

	# vertices del paralelogramo
	s1 = np.array(center) - l1 * 0.5 * v1 - l2 * 0.5 * v2
	print(f"La primera esquina es: {s1}")
	s2 = np.array(center) + l1 * 0.5 * v1 - l2 * 0.5 * v2
	print(f"La segunda esquina es: {s2}")
	s3 = np.array(center) + l1 * 0.5 * v1 + l2 * 0.5 * v2
	print(f"La tercera esquina es: {s3}")
	s4 = np.array(center) - l1 * 0.5 * v1 + l2 * 0.5 * v2
	print(f"La cuarta esquina es: {s4}")
	points = np.zeros((4*(steps+1)+1, 3))
	print(points)

	# Generamos los puntos de cada segmento
	for i in range(steps+1):
		x1 = l1 / steps * i
		print(f"\nX1 es: {x1}")		
		x2 = l2 / steps * i
		print(f"X2 es: {x2}")	
		points[i,:] = x1 * v1 + s1
		points[steps+1+i,:] = x2 * v2 + s2
		points[2*steps+2+i,:] = -x1 * v1 + s3
		points[3*steps+3+i,:] = -x2 * v2 + s4
		points[-1,:] = s1 #repetimos el primer punto porque es una figura cerrada
		#print(f"Los puntos son: \n{points}")
	# Devolvemos el array que contiene los puntos del segmento
	return points

v1=[-1,0,0]
v2=[0,1,0]
l1=10
l2=10
steps=1
paral = (create_paralelogram(0,v1,v2,l1,l2,steps))
print(paral)
plt.plot(paral[:,0],paral[:,1], linewidth=2.0, marker='o')
plt.grid()
plt.show()
