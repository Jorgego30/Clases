#!/usr/bin/env python
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Funcion que convierte un eje de rotacion en matriz antisimetrica 3x3 (so3)
def VecToso3(w): 
	return sp.Matrix([[0,-w[2],w[1]], [w[2],0,-w[0]], [-w[1],w[0],0]])

# Definimos ejes de rotacion de las articulaciones en la posicion cero del robot
w=[]
w.append(np.array([0,0,1]))
w.append(np.array([0,-1,0]))
w.append(np.array([0,-1,0]))
w.append(np.array([1,0,0]))
w.append(np.array([0,-1,0]))
w.append(np.array([1,0,0]))

# Definimos los eslabones
scalefactor=0.001 # para cambiar las unidades a metros
L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])*scalefactor

# Definimos los vectores que van del centro de cada eje al centro del siguiente
q=[]
q.append(np.array([0,0,L[0]]))
q.append(np.array([0,0,L[1]]))
q.append(np.array([0,0,L[2]]))
q.append(np.array([L[4],0,L[3]]))
q.append(np.array([L[5],0,0]))
q.append(np.array([L[6],0,L[7]]))

# Coordenadas de las articulaciones
t=sp.symbols('t0, t1, t2, t3, t4, t5')

# Calculamos las matrices de rotacion a partir de los ejes w, utilizando la formula de Rodrigues
R=[]

for i in range(0,6,1):
	antisimetrica_w = VecToso3(w[i])
	R.append(sp.eye(3)+sp.sin(t[i])*antisimetrica_w+(1-sp.cos(t[i]))*(antisimetrica_w*antisimetrica_w))

# Aplicamos rotaciones a los vectores q y w para llevarlos a la configuracion deseada
qs=[]; ws=[]; Ri=R[0]
qs.append(sp.Matrix(q[0]))
ws.append(sp.Matrix(w[0]))

for i in range(1,6,1):
	ws.append(Ri*sp.Matrix(w[i]))
	qs.append(Ri*sp.Matrix(q[i])+qs[i-1])
	Ri=Ri*R[i]

# Calculamos las velocidades lineales, los vectores giro correspondientes y la matriz Jacobiana
vs=[]; Ji=[]
i=0
vs.append(qs[i].cross(ws[i]))
Ji.append(ws[i].row_insert(3,vs[i]))
J=Ji[0]

for i in range(1,6,1):
	vs.append(qs[i].cross(ws[i]))
	Ji.append(ws[i].row_insert(3,vs[i]))
	J=J.col_insert(i,Ji[i])

Jp0=np.array(J.subs({t[0]:0, t[1]:0, t[2]:0, t[3]:0, t[4]:0, t[5]:0}), dtype=float)
"""
Jespecifica0 = sp.solve(J.subs({t[1]:0, t[2]:0, t[3]:0}).det())
Jespecifica2 = sp.solve(J.subs({t[1]:0, t[3]:0, t[4]:0}).det())
Jespecifica3 = sp.solve(J.subs({t[1]:0, t[4]:0, t[5]:0}).det())
Jespecifica4 = sp.solve(J.subs({t[1]:0, t[2]:0, t[4]:0}).det())
Jespecifica5 = sp.solve(J.subs({t[1]:0, t[2]:0, t[5]:0}).det())
# Jespecifica6 = sp.solve(J.subs({t[1]:0, t[3]:0, t[5]:0}).det()) Tiempo de ejecucion muy largo

Jespecifica7 = sp.solve(J.subs({t[0]:0, t[1]:0, t[2]:0}).det())

Jespecifica1 = sp.solve(J.subs({t[2]:0, t[3]:0, t[4]:0}).det())
# Jespecifica8 = sp.solve(J.subs({t[0]:0, t[1]:0, t[3]:0}).det()) Tiempo de ejecucion muy largo
Jlineal0_5 = sp.solve(J.subs({t[0]:0, t[1]:0, t[3]:0, t[5]:0}).det())
"""


"""
print(Jespecifica0)
print(Jespecifica1)
print(Jespecifica2)
print(Jespecifica3)
print(Jespecifica4)
print(Jespecifica5)
# print(Jespecifica6) Tiempo de ejecucion muy largo
print(Jespecifica7)
print(Jespecifica8)
print(Jlineal0_5)
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
	vjoints=np.array([0,xx[i],yy[i],0,0,0])
	giro.append(np.dot(Jp0,vjoints))

giro=np.array(giro)
print(giro)

# Calculamos los vectores llave, multiplicando por la inversa de la traspuesta de J
llave=[]
Jp0_T=np.linalg.inv(np.transpose(Jp0))
for i in range(0,400,1):
	taujoints=np.array([0,xx[i],yy[i],0,0,0])
	llave.append(np.dot(Jp0_T,taujoints))
llave=np.array(llave)

wx=giro[:,0]; wy=giro[:,1]; wz=giro[:,2]
vx=giro[:,3]; vy=giro[:,4]; vz=giro[:,5]

fwx=llave[:,0]; fwy=llave[:,1]; fwz=llave[:,2]
fvx=llave[:,3]; fvy=llave[:,4]; fvz=llave[:,5]
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










