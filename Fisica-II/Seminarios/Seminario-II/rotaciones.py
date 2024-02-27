import numpy as np

global pi
pi = np.pi

def Rotx(x):
	
	c = np.cos(x)
	s = np.sin(x)

	matrizX = np.zeros((3,3))
	matrizX[0][0] = 1
	matrizX[1][1] = c
	matrizX[1][2] = -s
	matrizX[2][1] = s
	matrizX[2][2] = c

	return np.round(matrizX,3)

def Roty(x):
	
	c = np.cos(x)
	s = np.sin(x)

	matrizY = np.zeros((3,3))
	matrizY[0][0] = c
	matrizY[0][2] = s
	matrizY[1][1] = 1
	matrizY[2][0] = -s
	matrizY[2][2] = c

	return np.round(matrizY,3)

def Rotz(x):
	
	c = np.cos(x)
	s = np.sin(x)

	matrizZ = np.zeros((3,3))
	matrizZ[0][0] = c
	matrizZ[0][1] = -s
	matrizZ[1][0] = s
	matrizZ[1][1] = c
	matrizZ[2][2] = 1

	return np.round(matrizZ,3)

def Rotv(eje,v,x):
	
	if(eje.lower()=='x'):
		return np.dot(Rotx(x),v)
	elif(eje.lower()=='y'):
		return np.dot(Roty(x),v)
	elif(eje.lower()=='z'):
		return np.dot(Rotz(x),v)

print(Rotv('x',[1,1,1],pi))