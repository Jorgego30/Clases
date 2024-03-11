import sympy as sp
#Definicıon de variables simbolicas
t1=sp.var("t1") # theta1
t2=sp.var("t2") # theta2
L1=sp.var("L1") # longitud del primer eslabon
L2=sp.var("L2") # longitud del segundo eslabon

# Elementos de la matriz Jacobiana

a=-L1*sp.sin(t1)-L2*sp.sin(t1+t2)
b=L1*sp.cos(t1)+L2*sp.cos(t1+t2)
c=-L2*sp.sin(t1+t2)
d=L2*sp.cos(t1+t2)
m=sp.Matrix([[a,c],[b,d]]) # Matriz Jacobiana
print(m)
m1 = sp.solve(m.det()) # Resolucion del determinante
print(m1)
m2 = sp.solve(m.subs({t1:0, L1:1, L2:1}).det())
print(m2)
