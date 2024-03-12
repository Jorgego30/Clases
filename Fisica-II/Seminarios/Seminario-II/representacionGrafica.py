import numpy as np
import matplotlib.pyplot as plt
# Definir el vector original
vector_original = np.array([10, 10, 10])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Dibujar el vector original en rojo
ax.quiver(0, 0, 0, vector_original[0], vector_original[1], vector_original[2], color='r', label='Original')
# Rotar el vector en incrementos de 10 grados y dibujar cada vector rotado
for angulo in range(20, 350, 20):
    angulo_rad = np.radians(angulo)
    matriz_rotacion = np.array([[np.cos(angulo_rad), -np.sin(angulo_rad), 0],[np.sin(angulo_rad), np.cos(angulo_rad), 0],[0, 0, 1]])
    vector_rotado = np.dot(matriz_rotacion, vector_original)
    # Dibujar el vector rotado
    ax.quiver(0, 0, 0, vector_rotado[0], vector_rotado[1], vector_rotado[2], color='b')
    # Establecer los límites de la gráfica
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([0, 8])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()