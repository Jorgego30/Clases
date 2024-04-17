import yaml, numpy as np

with open('robot.yaml', 'r') as file:
	robotdata = yaml.safe_load(file)

robotname = robotdata['robot']['name']
eslabones = robotdata['robot']['links']

joint_coords = np.array([0,0,0])

for eslabon in eslabones:
	print("eslabón ID = ", eslabon['id'])
	print("tipo de eslabón = ", eslabon['type'])
	print("coordenadas articulación = ", eslabon['joint_coords'])
	a = np.array([eslabon['joint_coords']])
	np.vstack((joint_coords,a))
	print("Eje rotación (R) o expansión (P) = ", eslabon['joint_axis'])



print(joint_coords)
