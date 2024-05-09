import yaml
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom
import numpy as np

# Leer el archivo YAML
with open('robot.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Iniciar la construcción del archivo URDF
robot = Element('robot', attrib={'name': data['robot']['name']})

# Materiales predeterminados
materials = [
    Element('material', attrib={'name': 'blue'}),
    Element('material', attrib={'name': 'black'}),
    Element('material', attrib={'name': 'red'})
]
colors = [
    SubElement(materials[0], 'color', attrib={'rgba': '0 0 0.8 1'}),
    SubElement(materials[1], 'color', attrib={'rgba': '0 0 0 1'}),
    SubElement(materials[2], 'color', attrib={'rgba': '0.8 0 0 1'})
]

for m in materials:
    robot.append(m)

# Base link
link0 = Element('link', attrib={'name': 'link0'})
visual = SubElement(link0, 'visual')
origin = SubElement(visual, 'origin', attrib={'xyz': '0 0 0.05', 'rpy': '0 0 0'})
geometry = SubElement(visual, 'geometry')
cylinder = SubElement(geometry, 'cylinder', attrib={'length': '0.1', 'radius': '0.1'})
material = SubElement(visual, 'material', attrib={'name': 'black'})
robot.append(link0)

# Crear enlaces y articulaciones
previous_link_orientation = np.array([0,0,0])
total_link_rotation=np.array([0,0,0])
for i, link in enumerate(data['robot']['links']):
    current_link_orientation=np.array(link['link_orientation'])
    link_rotation = np.cross(previous_link_orientation, current_link_orientation)
    angle=np.arccos(np.dot(previous_link_orientation, current_link_orientation))
    link_rotation = link_rotation * angle
    total_link_rotation=total_link_rotation+link_rotation
    previous_link_orientation = current_link_orientation
    
    xyz = np.array(link['link_orientation']) * link['length']/2

    link_element = Element('link', attrib={'name': f"link{i+1}"})
    visual = SubElement(link_element, 'visual')
    origin = SubElement(visual, 'origin', attrib={'xyz': ' '.join(map(str, xyz)), 'rpy': ' '.join(map(str, total_link_rotation))})
    geometry = SubElement(visual, 'geometry')
    if link['type'] == 'revolute':
        cylinder = SubElement(geometry, 'cylinder', attrib={'length': str(link['length']), 'radius': '0.05'})
    elif link['type'] == 'prismatic':
        box = SubElement(geometry, 'box', attrib={'size': f"0.1 0.1 {link['length']}"})
    material = SubElement(visual, 'material', attrib={'name': 'blue' if i % 2 == 0 else 'red'})
    robot.append(link_element)

    joint = Element('joint', attrib={'name': f"joint{i+1}", 'type': link['type']})
    parent = SubElement(joint, 'parent', attrib={'link': f"link{i}"})
    child = SubElement(joint, 'child', attrib={'link': f"link{i+1}"})
    origin = SubElement(joint, 'origin', attrib={'xyz': ' '.join(map(str, link['joint_coords'])), 'rpy': '0 0 0'})
    joint_axis = SubElement(joint, 'axis', attrib={'xyz': ' '.join(map(str, link['joint_axis']))})
    limit = SubElement(joint, 'limit', attrib={'lower': '-1.57', 'upper': '1.57', 'effort': '100.0', 'velocity': '1.0'})
    robot.append(joint)

# Serializar y guardar el archivo URDF
xmlstr = minidom.parseString(tostring(robot)).toprettyxml(indent="   ")
with open("robot.urdf", "w") as f:
    f.write(xmlstr)
