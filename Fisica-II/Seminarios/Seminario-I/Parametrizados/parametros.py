#!/usr/bin/env python
#
# By Angel.Pineiro at usc.es
# Version September, 2021
#
# EJEMPLO DE USO:
# python mkplots.py -c [0,0,0] -d 8 -s 10
#
#
import numpy as np
import matplotlib.pyplot as plt
import optparse
from mylib import *
desc="Codigo Python parametrizado."
def main():
	parser = optparse.OptionParser(description=desc, version='%prog version 1.0')
	parser.add_option('-c', '--center', help='Centro de la figura', action='store')
	parser.add_option('-d', '--dimension', help='Longitud de los segmentos o radio del polıgono', actioparser.add_option('-s', '--steps', help='Numero de puntos', action='store'))
	parser.set_defaults(center='0 0 0', dimension=8, steps=10)
	options, arguments = parser.parse_args()
#**************************************************************************************
	c_i=str(options.center).split()
	center=[]
	for i in range (0,3,1): center.append(np.float(c_i[i]))
	
	print(center)

	dir_vector=[1,1,0]
	length=float(options.dimension)
	l1=length
	l2=length
	radius=length
	steps=int(options.steps)
	v1=[0,1,0]
	v2=[1,0,0]
	normal_vector=[0,0,1]
	line = create_line(center, dir_vector, length, steps)
	paral = create_paralelogram(center, v1, v2, l1, l2, steps)
	polygon = create_polygon(center, normal_vector, radius, steps)
	# Generamos grafica con cırculo y elipses
	plt.plot(line[:,0],line[:,1], linewidth=2.0)
	plt.plot(paral[:,0],paral[:,1], linewidth=2.0)
	plt.plot(polygon[:,0],polygon[:,1], linewidth=2.0)
	limitplot=8
	plt.ylim(top = limitplot, bottom = -limitplot)
	plt.xlim(left = limitplot, right = -limitplot)
	plt.xticks(fontsize= 15)
	plt.yticks(fontsize= 15)
	plt.tight_layout()
	plt.show()

if __name__=="__main__" :
	main()
