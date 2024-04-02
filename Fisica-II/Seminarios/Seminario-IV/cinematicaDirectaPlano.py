import numpy as np
from optparse import OptionParser
import matplotlib.pyplot as plt

def robot_structure():
	# Estructura del robot
	
	#Se definen los ejes de rotacion
	axis1 = np.array([0, 0, 1]) # Eje de rotación de la primera articulación
	axis2 = np.array([0, 0, 1]) # Eje de rotación de la segunda articulación
	axis3 = np.array([0, 0, 1]) # Eje de rotación de la tercera articulación

	#Se definen las posiciones de las articulaciones
	q1 = np.array([0, 0, 0]) # Posición de la primera articulación
	q2 = np.array([1, 0, 0]) # Posición de la segunda articulación
	q3 = np.array([2, 0, 0]) # Posición de la tercera articulación
	
	#Se calculan las velocidades (Producto escalar de la posicion de la articulacion con su eje de rotacion)
	v1 = np.cross(q1, axis1) #Velocidad lineal de la primera articulacion
	v2= np.cross(q2, axis2) #Velocidad lineal de la segunda articulacion
	v3= np.cross(q3, axis3) #Velocidad lineal de la tercera articulacion

	# Ejes helicoidales
	# np.hstack concatena dos vectores
	S1 = np.hstack((axis1, v1)) # Eje helicoidal de la primera articulación
	S2 = np.hstack((axis2, v2)) # Eje helicoidal de la segunda articulación
	S3 = np.hstack((axis3, v3)) # Eje helicoidal de la tercera articulación
	
	# Matriz de transformación homogénea en la posición cero del robot

	#Se define el vector de translacion	
	p = np.array([3, 0, 0])
	
	#Se define la matriz homogenea de rotacion (T_matrix es una funcion creada posteriormente)
	M0 = T_matrix(np.eye(3), p)
	return S1, S2, S3, M0


# Calcula la matriz antisimétrica de un vector R3
def antisymR3(v): 
	return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])


# Devuelve la matriz de rotación para un eje y un ángulo dados usando la fórmula de Rodrigues
def R_matrix(axis, angle):	
	# El ángulo ha de estar en radianes
	axis = axis/np.linalg.norm(axis)

	#Se crea la matriz antisimetrica del vector dado
	amatrix = antisymR3(axis)

	#Se calcula la matriz de rotacion
	matriz = np.eye(3) + np.sin(angle)*amatrix + (1-np.cos(angle))*np.dot(amatrix, amatrix)
	return matriz

# Devuelve la matriz de transformación homogénea a partir de una matriz de rotación y un vector de traslación
def T_matrix(R, p):
	# np.vstack añade un vector al final de una matriz. .reshape transpone un vector
	matriz = np.vstack((np.hstack((R, p.reshape(3,1))), np.array([0, 0, 0, 1])))
	return matriz

# Calcula la matriz exponencial a partir de un eje helicoidal y de un ángulo de rotación
def exp_matrix(S, theta):
	w = S[0:3] # Eje de rotación del eje helicoidal
	v = S[3:6] # Velocidad lineal del eje helicoidal
	R = R_matrix(w, theta) # Matriz de rotación

	#Se crea la matriz antisimetrica del eje helicoidal
	wmatrix = antisymR3(w)

	# Vector de traslación
	p = (np.eye(3)*theta + (1-np.cos(theta))*wmatrix + (theta-np.sin(theta))*np.dot(wmatrix, wmatrix)) @ v
	return T_matrix(R, p)

#Se preparan las opciones para que el codigo pueda recibir parametros
parser = OptionParser()
parser.add_option("-a", "--a1", type="float", default=90, help="Ángulo de rotación para la primera articulación (grados)")
parser.add_option("-b", "--a2", type="float", default=-90, help="Ángulo de rotación para la segunda articulación (grados)")
parser.add_option("-c", "--a3", type="float", default=90, help="Ángulo de rotación para la tercera articulación (grados)")
(options, args) = parser.parse_args()

#Se pasan los angulos a radianes
a1 = np.deg2rad(options.a1) # Ángulo de rotación de la primera articulación
a2 = np.deg2rad(options.a2) # Ángulo de rotación de la segunda articulación
a3 = np.deg2rad(options.a3) # Ángulo de rotación de la tercera articulación

#Se reciben los datos de la estructura del robot
S1, S2, S3, M0 = robot_structure()

#Se definen las matrices de transformacion homogeneas para las articulaciones del robot
T1 = exp_matrix(S1, a1) # Matriz de transformación homogénea para la primera articulación
T2 = exp_matrix(S2, a2) # Matriz de transformación homogénea para la segunda articulación
T3 = exp_matrix(S3, a3) # Matriz de transformación homogénea para la segunda articulación

# Matriz de transformación homogénea para la posición final del robot
M = T1 @ T2 @ T3 @ M0 

# Dado que es un movimiento en 2D, representamos la posición final del robot en el plano XY
fig = plt.figure()
ax = fig.add_subplot(111)

# Definimos el origen y el final de cada eslabón en la posición cero y en la posición final del robot
p10ini = np.array([0, 0, 0, 1])
p11ini = np.array([1, 0, 0, 1])
p20ini = p11ini
p21ini = np.array([2, 0, 0, 1])
p30ini = p21ini
p31ini = np.array([3, 0, 0, 1])
p10fin = p10ini
p11fin = T1 @ p11ini
p20fin = p11fin
p21fin = T1 @ T2 @ p21ini
p30fin = p21fin
p31fin = T1 @ T2 @ T3 @ p31ini

# Dibuja el primer eslabón en posicion 0
ax.plot([p10ini[0], p11ini[0]], [p10ini[1], p11ini[1]], 'r', linewidth=4)
# Dibuja el primer eslabon rotado
ax.plot([p10fin[0], p11fin[0]], [p10fin[1], p11fin[1]], 'r', linewidth=4)

# Dibuja el segundo eslabón
ax.plot([p20ini[0], p21ini[0]], [p20ini[1], p21ini[1]], 'g', linewidth=4)
# Dibuja el segundo eslabon rotado 
ax.plot([p20fin[0], p21fin[0]], [p20fin[1], p21fin[1]], 'g', linewidth=4)

# Dibuja el tercer eslabón
ax.plot([p30ini[0], p31ini[0]], [p30ini[1], p31ini[1]], 'y', linewidth=4)
# Dibuja el tercer eslabon rotado
ax.plot([p30fin[0], p31fin[0]], [p30fin[1], p31fin[1]], 'y', linewidth=4)

# Dibuja los puntos de interés
ax.plot(p10ini[0], p10ini[1], 'bo', markersize=10) # punto inicial de L1
ax.plot(p11ini[0], p11ini[1], 'ro', markersize=10) # punto final de L1 en la posición inicial
ax.plot(p11fin[0], p11fin[1], 'ro', markersize=10) # punto final de L1 en la posición final
ax.plot(p21ini[0], p21ini[1], 'go', markersize=10) # punto final de L2 en la posición inicial
ax.plot(p21fin[0], p21fin[1], 'go', markersize=10) # punto final de L2 en la posición final
ax.plot(p31ini[0], p31ini[1], 'y>', markersize=10) # punto final de L3 en la posición inicial
ax.plot(p31fin[0], p31fin[1], 'y^', markersize=10) # punto final de L3 en la posición final

# Ajusta el tamaño del gráfico y lo guarda
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_aspect('equal', 'box')
plt.tight_layout()
plt.savefig('3RPlano.png')

