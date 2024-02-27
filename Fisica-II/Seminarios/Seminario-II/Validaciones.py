from rotaciones import *

#Se valida que las matrices de las rotaciones sean unitarias

print("Primera validacion: ")

print(f"X:\n{Rotx(pi)*np.transpose(Rotx(pi))}\nDeterminante:{np.linalg.det(Rotx(pi))}")
print()

print(f"Y:\n{Roty(pi)*np.transpose(Roty(pi))}\nDeterminante:{np.linalg.det(Roty(pi))}")
print()

print(f"Z:\n{Rotz(pi)*np.transpose(Rotz(pi))}\nDeterminante:{np.linalg.det(Rotz(pi))}")
print()

#Se validan con un vector unitario

print("Segunda validacion: ")

v = np.array([1,1,1])
print(f"X:\n{Rotv('x',v,pi)*np.transpose(Rotv('x',v,pi))}")
print()

print(f"Y:\n{Rotv('y',v,pi)*np.transpose(Rotv('y',v,pi))}")
print()

print(f"Z:\n{Rotv('z',v,pi)*np.transpose(Rotv('z',v,pi))}")
print()

# 
print("Tercera validacion: ")

v = np.array([1,0,0])
print(f"X:\n{Rotv('x',v,pi)*np.transpose(Rotv('x',v,pi))}")
print()

print(f"Y:\n{Rotv('y',v,pi)*np.transpose(Rotv('y',v,pi))}")
print()

print(f"Z:\n{Rotv('z',v,pi)*np.transpose(Rotv('z',v,pi))}")
print()

#
print("Cuarta validacion: ")

v = np.array([0,1,0])
print(f"X:\n{Rotv('x',v,pi)*np.transpose(Rotv('x',v,pi))}")
print()

print(f"Y:\n{Rotv('y',v,pi)*np.transpose(Rotv('y',v,pi))}")
print()

print(f"Z:\n{Rotv('z',v,pi)*np.transpose(Rotv('z',v,pi))}")
print()

#
print("Segunda validacion: ")

v = np.array([0,0,1])
print(f"X:\n{Rotv('x',v,pi)*np.transpose(Rotv('x',v,pi))}")
print()

print(f"Y:\n{Rotv('y',v,pi)*np.transpose(Rotv('y',v,pi))}")
print()

print(f"Z:\n{Rotv('z',v,pi)*np.transpose(Rotv('z',v,pi))}")
print()