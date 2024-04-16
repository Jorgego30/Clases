import yaml
with open('robot.yaml', 'r') as file:
	robotdata = yaml.safe_load(file)

robotname = robotdata['robot']['name']
eslabones = robotdata['robot']['links']

for eslabon in eslabones:
	print("eslabón ID = ", eslabon['id'])
	print("tipo de eslabón = ", eslabon['type'])
	print("coordenadas articulación = ", eslabon['joint_coords'])
	print("Eje rotación (R) o expansión (P) = ", eslabon['joint_axis'])
