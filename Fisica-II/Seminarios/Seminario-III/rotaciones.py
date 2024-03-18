"""
[	1 0 0						[	w1  -w3  w2							[	w1  -w3  w2			²
	0 1 0		+ sen(angulo)		w3   0    0			+ cos(angulo)		w3   0    0
	0 0 1	]						-w2  0    0	  ]							-w2  0    0	  ]
"""
import numpy as np

global pi
pi = np.pi

def matrizAntisimetrica(vector):

    x = vector[0]
    y = vector[1]
    z = vector[2]

    matriz = np.array([[0,-z,y],[z,0,-x],[-y,x,0]])

    return matriz

def rotacionRodrigues(eje,angulo):
	s = np.round(np.sin(angulo),3)
	c = np.round(np.cos(angulo),3)
	print(s)
	print(c)

	matrizIdentidad = np.eye(3)
	print(matrizIdentidad)

#

	matriz = matrizAntisimetrica(eje)

	cuadrado = np.dot(matriz,matriz)
	print(cuadrado)
	
	print(s*matriz)
	print((1-c)*cuadrado)
	print(s*matriz+(1-c)*cuadrado)
	
	matrizResultado = (matrizIdentidad + s*matriz + (1-c)*cuadrado)

	return np.round(matrizResultado,3)

def matrizLogaritmo(matriz):

	matrizIdentidad = np.eye(3)

	traza = np.trace(matriz)
	
	if traza>=3:

		return "El angulo es: 0\nEl vector no esta definido" 

	elif (traza <= -1):
		angulo = pi
		primerVector = np.array([matriz[0][2],matriz[1][2], 1+matriz[2][2]])
		segundoVector = np.array([matriz[0][1],1+matriz[1][1],matriz[2][1]])
		tercerVector = np.array([1+matriz[0][0],matriz[1][0], matriz[2][0]])

		if (1+matriz[2][2])!=0:
			eje = (1/(sqrt(2*(1+matriz[2][2]))))*primerVector
		
		if (1+matriz[1][1]):
			eje2 = (1/(sqrt(2*(1+matriz[1][1]))))*segundoVector

		if (1+matriz[0][0]):
			eje3 = (1/(sqrt(2*(1+matriz[0][0]))))*tercerVector
		
		return f"El angulo es {angulo}\nHay 3 posibilidades para el vector\n1.- {eje}\n2.- {eje2}\n3.- {eje3}"
	
	else:
		c = np.round(np.arccos(0.5*(traza-1)),3)
		angulo = c
		s = np.round(np.sin(angulo),3)		
		transpuesta = np.transpose(matriz)

		matrizAntisimetrica = np.array(pow((2*s),-1)*(matriz-transpuesta)) 
		x = matrizAntisimetrica[0][0] 
		y = matrizAntisimetrica[0][2]
		z = -matrizAntisimetrica[0][1]		
		eje = np.array([x,y,z])

		return f"EL angulo es: {np.round(np.degrees(angulo))}\nEl eje es: {eje}"


