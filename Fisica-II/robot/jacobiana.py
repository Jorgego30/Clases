#!/usr/bin/env python
from lecturaRobot import *
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Funcion que convierte un eje de rotacion en matriz antisimetrica 3x3 (so3)
def VecToso3(w): 
	return sp.Matrix([[0,-w[2],w[1]], [w[2],0,-w[0]], [-w[1],w[0],0]])

ids , q, w = leer()
numberOfIds = len(ids)

# Definimos ejes de rotacion de las articulaciones en la posicion cero del robot
print("Ejes de rotacion:\n",w)

# Definimos los eslabones
scalefactor = 0.001
L=np.array([50, 50, 100, 50, 100, 50, 70]) * scalefactor

# Definimos los vectores que van del centro de cada eje al centro del siguiente
print("Vectores de posicion:\n", q)
print()

# Coordenadas de las articulaciones
t=sp.symbols('t0, t1, t2, t3, t4, t5, t6')

# Calculamos las matrices de rotacion a partir de los ejes w, utilizando la formula de Rodrigues
R=[]

for i in range(0, numberOfIds, 1):
	antisimetrica_w = VecToso3(w[i])
	R.append(sp.eye(3)+sp.sin(t[i])*antisimetrica_w+(1-sp.cos(t[i]))*(antisimetrica_w*antisimetrica_w))

# Aplicamos rotaciones a los vectores q y w para llevarlos a la configuracion deseada
qs=[]; ws=[]; Ri=R[0]
qs.append(sp.Matrix(q[0]))
ws.append(sp.Matrix(w[0]))

print("Ejes de giro: ",ws)
print("Vectores posicion: ",qs)	
print()

for i in range(1, numberOfIds, 1):
	ws.append(Ri*sp.Matrix(w[i]))
	qs.append(Ri*sp.Matrix(q[i])+qs[i-1])
	Ri=Ri*R[i]

# Calculamos las velocidades lineales, los vectores giro correspondientes y la matriz Jacobiana
vs=[]; Ji=[]
i=0
vs.append(qs[i].cross(ws[i]))
Ji.append(ws[i].row_insert(3,vs[i]))
J=Ji[0]

print("Velocidad lineal:\n",vs)
print("\nMatriz:\n", J)
print()

for i in range(1, numberOfIds, 1):
	vs.append(qs[i].cross(ws[i]))
	Ji.append(ws[i].row_insert(3,vs[i]))
	J=J.col_insert(i,Ji[i])

print(J)

Jp0=np.array(J.subs({t[0]:0, t[1]:0, t[2]:0, t[3]:0, t[4]:0, t[5]:0, t[6]:0}), dtype=float)
print("Matriz Jacobiana en posicion 0:\n", Jp0)

print("Algunas configuraciones singulares:")

rango_J=J.rank()
condicion=sp.Eq(rango_J, 5) # esta seria la condición para que tengas una singularidad -> rango menor a 6


singularidades=sp.solve(condicion, (t[0]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2]))
print(singularidades)
singularidades=sp.solve(condicion, (t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[0], t[1]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[2]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[1], t[2]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[2], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[3], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[3], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[3], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[4], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[0], t[1], t[2]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[0], t[2], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[2], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[2], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[2], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[3], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[3], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[3], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[5], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[1], t[2]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[1], t[2], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[1], t[3], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[3], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[3], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[1], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[1], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[2], t[3], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[3], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[3], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[2], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[2], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[3], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[3], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[3], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[4], t[5], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[3]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[1], t[3], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[3], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[3], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[1], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[1], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[1], t[2], t[3], t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[3], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[3], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[1], t[2], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[1], t[2], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[2], t[3], t[4], t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[2], t[3], t[4], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[2], t[3], t[5], t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[2], t[4], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[3], t[4], t[5], t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[3],t[4]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[3],t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[3],t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[2], t[3], t[4],t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[0], t[2], t[3], t[4],t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[3], t[4], t[5],t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[1], t[2], t[3], t[4],t[5]))
print(singularidades)
singularidades=sp.solve(condicion, (t[1], t[2], t[3], t[4],t[6]))
print(singularidades)

singularidades=sp.solve(condicion, (t[1], t[3], t[4], t[5],t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[2], t[3], t[4], t[5],t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[3], t[4],t[5]))
print(singularidades)

singularidades=sp.solve(condicion, (t[0], t[2], t[3], t[4], t[5],t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[1], t[2], t[3], t[4], t[5],t[6]))
print(singularidades)


singularidades=sp.solve(condicion, (t[0], t[1], t[2], t[3], t[4], t[5],t[6]))
print(singularidades)

"""
radio = 1
u = np.linspace(0,2*np.pi,100)
x=[]
y=[]

for i in range (0,100,1):
	x.append(radio * np.cos(u[i]))
	y.append(radio * np.sin(u[i]))

x = np.array(x)
xx=np.r_[np.r_[x,-x], np.r_[-x,x]]

y = np.array(y)
yy=np.r_[np.r_[y,-y], np.r_[-y,y]]


# Calculamos los vectores giro, multiplicando por la Matriz Jacobiana
giro=[]
for i in range(0,400,1):
	vjoints=np.array([0,xx[i],yy[i],0,0,0,0])
	giro.append(np.dot(Jp0,vjoints))

giro=np.array(giro)
print(giro)

# Calculamos los vectores llave, multiplicando por la inversa de la traspuesta de J
llave=[]
Jp0_T=np.linalg.inv(np.transpose(Jp0))

for i in range(0,400,1):
	taujoints=np.array([0,xx[i],yy[i],0,0,0,0])
	llave.append(np.dot(Jp0_T,taujoints))
llave=np.array(llave)

wx=giro[:,0]; wy=giro[:,1]; wz=giro[:,2]
vx=giro[:,3]; vy=giro[:,4]; vz=giro[:,5]

fwx=llave[:,0]; fwy=llave[:,1]; fwz=llave[:,2]
fvx=llave[:,3]; fvy=llave[:,4]; fvz=llave[:,5]

"""
# Generamos grafica con cırculo y elipses
"""
fig,ax = plt.subplots(2,2)
ax[0,0].plot(wx, wy)
ax[0,0].plot(wx, wz)
ax[0,0].plot(wy, wz)
limitplot=8
plt.ylim(top = limitplot, bottom = -limitplot)
plt.xlim(left = limitplot, right = -limitplot)
plt.xticks(fontsize= 15)
plt.yticks(fontsize= 15)
plt.tight_layout()
"""
"""
plt.scatter(wx,wy, label='WX/WY')
plt.scatter(wx,wz, label='WX/WZ')
plt.scatter(wy,wz, label='WY/WZ')
limitplot=8
plt.ylim(top = limitplot, bottom = -limitplot)
plt.xlim(left = limitplot, right = -limitplot)
plt.xticks(fontsize= 10)
plt.yticks(fontsize= 10)
plt.tight_layout()
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

plt.scatter(vx,vy, label='VX/VY')
plt.scatter(vx,vz, label='VX/VZ')
plt.scatter(vy,vz, label='VY/VZ')
plt.ylim(top = limitplot, bottom = -limitplot)
plt.xlim(left = limitplot, right = -limitplot)
plt.xticks(fontsize= 10)
plt.yticks(fontsize= 10)
plt.tight_layout()
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

plt.scatter(fwx,fwy, label='MX/MY')
plt.scatter(fwx,fwz, label='MX/MZ')
plt.scatter(fwy,fwz, label='MY/MZ')
plt.ylim(top = limitplot, bottom = -limitplot)
plt.xlim(left = limitplot, right = -limitplot)
plt.xticks(fontsize= 10)
plt.yticks(fontsize= 10)
plt.tight_layout()
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()

plt.scatter(fvx,fvy, label='FX/FY')
plt.scatter(fvx,fvz, label='FX/FZ')
plt.scatter(fvy,fvz, label='FY/FZ')

plt.ylim(top = limitplot, bottom = -limitplot)
plt.xlim(left = limitplot, right = -limitplot)
plt.xticks(fontsize= 10)
plt.yticks(fontsize= 10)
plt.tight_layout()
plt.legend(loc='upper right', shadow=True, fontsize='x-large')
plt.show()


# plt.save("Posicion0.jpg)
"""

