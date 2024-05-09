from lecturaRobot import *
import numpy as np
import optparse

desc="Resolucion del problema cinematico directo para el Robot Niryo One."

# Convierte un vector de 3 componentes en una matriz antisimetrica
def VecToso3(omg):
	return np.array([[0, -omg[2], omg[1]], [omg[2], 0, -omg[0]], [-omg[1], omg[0], 0]])

# convierte un vector giro o eje helicoidal en matriz 4x4 se3
def VecTose3(V):
	return np.r_[np.c_[VecToso3([V[0], V[1], V[2]]), [V[3], V[4], V[5]]], np.zeros((1, 4))]

# extrae un vector de 3 componentes de una matriz antisimetrica so3
def so3ToVec(so3mat): 
	return np.array([so3mat[2][1], so3mat[0][2], so3mat[1][0]])

# convierte matriz se3 en una matriz de transformacion homogenea a traves de la exponencial
def MatrixExp6(se3mat):
	se3mat = np.array(se3mat) # vector giro en representacion matricial se3 (4x4)
	v=se3mat[0: 3, 3] # extraemos el vector v*theta (velocidad lineal)
	omgmattheta=se3mat[0: 3, 0: 3] # extraemos omega*theta en forma matricial 3x3 (so3)
	omgtheta = so3ToVec(omgmattheta) # lo pasamos a forma vectorial
	if (np.linalg.norm(omgtheta))<1.e-6: # en el caso de que no haya giro (omega despreciable)
		return np.r_[np.c_[np.eye(3), v], [[0, 0, 0, 1]]] # concatena columnas y filas. Solo traslacion
	else: # caso general
		theta = np.linalg.norm(omgtheta)
		omgmat = omgmattheta / theta # omega en forma matricial 3x3 (so3) Normalizada
		# a continuacion aplicamos la definicion de matriz exponencial que vimos en clase (slide 42)
		G_theta=np.eye(3)*theta+(1-np.cos(theta))*omgmat+(theta-np.sin(theta))*np.dot(omgmat,omgmat)
		R=np.eye(3)+np.sin(theta)*omgmat+(1.-np.cos(theta))*np.dot(omgmat,omgmat)
		return np.r_[np.c_[R,np.dot(G_theta,v)/theta],[[0, 0, 0, 1]]]

def R2Euler(R):
	sy=np.sqrt(R[0,0]*R[0,0]+R[1,0]*R[1,0])
	singular=sy<1.e-6
	if not singular:
		x=np.arctan2(R[2,1],R[2,2])
		y=np.arctan2(-R[2,0],sy)
		z=np.arctan2(R[1,0],R[0,0])
	else:
		x=np.arctan2(-R[1,2],R[1,1])
		y=np.arctan2(-R[2,0],sy)
		z=0.
	return np.array([x,y,z])

def main():
	parser = optparse.OptionParser(description=desc, version='%prog version 1.0')
	parser.add_option('-j', '--joints', help='Coordenadas de las articulaciones', action='store')
	parser.set_defaults(joints='0 0 0 0 0 0 0')
	options, arguments = parser.parse_args()
	#**************************************************************************************
	joints=str(options.joints).split()
	t=[]

	ids, q, w = leer()
	numberOfIds = len(ids)

	print(q)

	#for i in range (0,6,1): t.append(np.deg2rad(float(joints[i])))
	for i in range (0, numberOfIds, 1): t.append((float(joints[i])))

	print("Coordenadas en radianes", np.round(t,5))

	# Definimos los eslabones
	# scalefactor=0.001 # por si quiero los resultados en otras unidades
	L=np.array([0.5, 0.5, 1, 0.5, 1, 0.5, 0.7])
	
	# Calculamos los ejes de giro y vectores posicion en la configuracion final del robot
	qs=[]; ws=[]
	qs.append(np.array(q[0]))
	ws.append(np.array(w[0]))

	for i in range(1,numberOfIds,1):
		ws.append(np.array(w[i]))
		qs.append(np.array(q[i])+qs[i-1])
	
	# Calculamos las velocidades lineales para construir los ejes helicoidales
	vs=[]; Si=[]
	
	for i in range(0, numberOfIds, 1):
		vs.append(np.cross(qs[i],ws[i]))
		Si.append(np.r_[ws[i],vs[i]])

	M=np.array([[1,0,0,L[6]+L[5]+L[4]],[0,1,0,0],[0,0,1,L[0]+L[1]+L[2]+L[3]],[0,0,0,1]])
	print (M)
	T=np.eye(4)
	
	for i in range(0,6,1):
		T=np.dot(T,MatrixExp6(VecTose3(Si[i]*t[i])))
	
	T=np.dot(T,M)
	
	print("\nMatriz de transformacion homogenea: \n", np.round(T, 3))
	
	print("\nCoordenadas (x,y,z) del TCP: ", np.round(T[0: 3, 3],3))
	
	R=(np.round(T[0: 3, 0: 3],3))

	print("\nAngulos de Euler en radianes", R2Euler(R))

	print("\nAngulos de Euler en grados:")

	print(np.array([np.rad2deg(R2Euler(R)[0]), np.rad2deg(R2Euler(R)[1]), np.rad2deg(R2Euler(R)[2])]))

if __name__=="__main__" :
	main()















































