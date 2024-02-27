import numpy as np

global pi
pi = np.pi

def Rotx(x):
	
	matrizX = np.zeros((3,3))
	matrizX[0][0] = 1
	matrizX[1][1] = np.cos(x)
	matrizX[1][2] = -np.sin(x)
	matrizX[2][1] = np.sin(x)
	matrizX[2][2] = np.cos(x)

	return matrizX

def Roty(x):
	
	matrizY = np.zeros((3,3))
	matrizY[0][0] = np.cos(x)
	matrizY[0][2] = np.sin(x)
	matrizY[1][1] = 1
	matrizY[2][0] = -np.sin(x)
	matrizY[2][2] = np.cos(x)

	return matrizY

def Rotz(x):
	
	matrizZ = np.zeros((3,3))
	matrizZ[0][0] = np.cos(x)
	matrizZ[0][1] = -np.sin(x)
	matrizZ[1][0] = np.sin(x)
	matrizZ[1][1] = np.cos(x)
	matrizZ[2][2] = 1

	return matrizZ

def rotacion(eje,v,x):
	
	if(eje.lower()=='x'):
		return v*Rotx(x)
	elif(eje.lower()=='y'):
		return v*Roty(x)
	elif(eje.lower()=='z'):
		return v*Rotz(x)


