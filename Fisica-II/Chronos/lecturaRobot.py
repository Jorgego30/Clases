import yaml, numpy as np
def leer():

	with open('robot.yaml', 'r') as file:
		robotdata = yaml.safe_load(file)

	robotname = robotdata['robot']['name']
	eslabones = robotdata['robot']['links']

	ids = []
	q = []
	w = []

	for eslabon in eslabones:
		# print("eslabón ID = ", eslabon['id'])
		ids.append(np.array(eslabon['id']))
		# print("tipo de eslabón = ", eslabon['type'])
		# print("coordenadas articulación = ", eslabon['joint_coords'])
		q.append(np.array(eslabon['joint_coords']))
		# print("Eje rotación (R) o expansión (P) = ", eslabon['joint_axis'])
		w.append(np.array(eslabon['joint_axis']))
		
	# print(q)
	# print(w)
	# print(L)

	return ids, q, w
