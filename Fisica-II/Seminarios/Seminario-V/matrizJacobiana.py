import sympy as sp
import numpy as np
2# calcula una matriz de transformación homogénea a partir de un eje helicoidal y un ángulo de rotación
def MatrixExp6sp(S,theta):
	w = sp.Matrix(S[0:3])
	v = sp.Matrix(S[3:6])
	omgmat = VecToso3sp(w)
	if (w.norm() < 10e-6):
		return sp.eye(3).row_join(v*theta).col_join(sp.transpose(sp.Matrix([0,0,0,1])))
	else:
		R = MatrixExp3sp(w,theta)
		G_theta=sp.eye(3) * theta + (1 - sp.cos(theta)) * omgmat + (theta - sp.sin(theta)) * (omgmat*omgmat)
		return R.row_join(G_theta*v).col_join(sp.transpose(sp.Matrix([0,0,0,1])))

# calcula una matriz de rotación a partir del eje y del ángulo de rotación
def MatrixExp3sp(w, theta):
	w = sp.Matrix(w).normalized()
	omgmat = VecToso3sp(w)
	return sp.eye(3) + (sp.sin(theta)*omgmat) + ((1-sp.cos(theta))*(omgmat*omgmat))

# transforma un vector de 3 componentes a matriz antisimétrica
def VecToso3sp(v):
	v = sp.Matrix(v)
	return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]],[-v[1], v[0], 0]])

# calcula la matriz adjunta de una matriz de transformación homogénea
def Adjunta(T):
	R, p = TransToRp(T)
	return R.row_join(sp.zeros(3)).col_join((VecToso3sp(p)*R).row_join(R))

# separa la matriz de rotación y el vector de traslación de una matriz de transformación homogénea
def TransToRp(T):
	return sp.Matrix(T[0:3,0:3]), sp.Matrix(T[0:3,3])

# Coordenadas de las articulaciones (suponiendo 6 dof)
t=sp.symbols('t0, t1, t2, t3, t4, t5')
