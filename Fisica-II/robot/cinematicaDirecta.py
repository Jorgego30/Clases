import yaml, numpy as np

with open('robot.yaml', 'r') as file:
	robotdata = yaml.safe_load(file)

robotname = robotdata['robot']['name']
eslabones = robotdata['robot']['links']

joint_coords = []
joint_axis = []
length = []

for eslabon in eslabones:
	print("eslabón ID = ", eslabon['id'])
	print("tipo de eslabón = ", eslabon['type'])
	print("coordenadas articulación = ", eslabon['joint_coords'])
	joint_coords.append(eslabon['joint_coords'])
	print("Eje rotación (R) o expansión (P) = ", eslabon['joint_axis'])
	joint_axis.append(eslabon['joint_axis'])
	print("longitud articulación = ", eslabon['length'])
	length.append(eslabon['length'])



print(joint_coords)
print(joint_axis)
print(length)

# Definimos los vectores que van de cada eje al siguiente
q = []
for i in length:
	q[i] = 
