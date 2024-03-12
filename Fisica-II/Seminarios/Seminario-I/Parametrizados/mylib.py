import numpy as np

def create_line(center, dir_vector, length, steps):
	v = np.array(dir_vector)
	v = v / np.linalg.norm(v)
	start = np.array(center) - length * 0.5 * v # punto inicial del segmento
	# El numero de steps define la resolucion del segmento
	points = np.zeros((steps+1, 3))
	# Generamos los puntos del segmento
	for i in range(steps+1):
		x = length / steps * i
		points[i,:] = x * v + start
	# Devolvemos el array que contiene los puntos del segmento
	return points

def create_paralelogram(center, v1, v2, l1, l2, steps):
	v1 = np.array(v1)
	v1 = v1 / np.linalg.norm(v1)
	v2 = np.array(v2)
	v2 = v2 / np.linalg.norm(v2)
	# vertices del paralelogramo
	s1 = np.array(center) - l1 * 0.5 * v1 - l2 * 0.5 * v2
	s2 = np.array(center) + l1 * 0.5 * v1 - l2 * 0.5 * v2
	s3 = np.array(center) + l1 * 0.5 * v1 + l2 * 0.5 * v2
	s4 = np.array(center) - l1 * 0.5 * v1 + l2 * 0.5 * v2
	points = np.zeros((4*(steps+1)+1, 3))
	# Generamos los puntos de cada segmento
	for i in range(steps+1):
		x1 = l1 / steps * i; x2 = l2 / steps * i;
		points[i,:] = x1 * v1 + s1
		points[steps+1+i,:] = x2 * v2 + s2
		points[2*steps+2+i,:] = -x1 * v1 + s3
		points[3*steps+3+i,:] = -x2 * v2 + s4
		points[-1,:] = s1 #repetimos el primer punto porque es una figura cerrada
	# Devolvemos el array que contiene los puntos del segmento
	return points

def create_polygon(center, normal_vector, radius, steps):
	n = np.array(normal_vector)
	n = n / np.linalg.norm(n)
	c = np.array(center)
	# Generamos un vector aleatorio no nulo y que no est´e alineado con n
	while True:
		temp = np.random.rand(3)
		if np.linalg.norm(temp) < 1e-5: continue
		temp = temp / np.linalg.norm(temp)
		if np.dot(temp, n) < 0.8: break
	# El producto vectorial de n y temp es un vector que va en la
	# direcci´on radial de la circunferencia que contiene al pol´ıgono
	u = np.cross(n, temp)
	# El producto vectorial del vector normal y del vector
	# radial es un vector tangente a la circunferencia
	v = np.cross(n, u)
	points = np.zeros((steps+1, 3))
	# Generamos los puntos del pol´ıgono
	for i in range(steps):
		angle = 2.0 * np.pi / steps * i
		points[i,:] = radius * (np.cos(angle) * u + np.sin(angle) * v) + c
		points[-1] = radius * u + c
	# Devolvemos el array que contiene los puntos del pol´ıgono
	return points

