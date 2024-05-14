#Dado el grafo de la figura, encuentra un árbol de expansión de coste mínimo describiendo el proceso paso a
#paso mediante el algoritmo de Prim
import os

grafo = {'h': [('j',3), ('z',2)],
         	'j': [('h',3),('z',4),('r',1)],
			'z': [('h',2),('j',4),('w',4)],
			'r': [('j',1),('w',1),('k',1),('y',1)],
			'w': [('r',1),('z',4)],
			'k': [('r',1), ('y',2),('t',6),('l',5)],
			'l': [('k',5),('t',2)],
            't': [('k',6),('y',5),('l',2)],
            'y': [('r',1),('t',5),('k',2)]
		}

##     CREAR LAS ESTRUCTURAS DE DATOS NECESARIAS PARA ALMACENAR
##     LOS DATOS NECESARIOS PARA EL ALGORITMO DE PRIM.
##     EN PYTHON ES MUY FÁCIL CREAR LISTAS Y DICCIONARIOS NECESARIOS
##     COMO SE MUESTRA A CONTINUACIÓN
listaVisitados = []
grafoResultante = {}
listaOrdenada = []

#    COMIENZO DEL ALGORITMO DE PRIM
#1.- ELEGIR NODO ORIGEN AL AZAR O PEDIRLO AL USUARIO
origen = input("\nIngresa el nodo origen: ")
#2.- AGREGARLO A LA LISTA DE VISITADOS
listaVisitados.append(origen)

#3.- AGREGAR SUS ADYACENTES A LA LISTA ORDENADA
for destino,peso in grafo[origen]:
  listaOrdenada.append((origen, destino, peso))
'''ORDENAMIENTO INSERT PARA LA LISTA'''
pos=0
act=0
listAux=[]
for i in range(len(listaOrdenada)):
    listAux=listaOrdenada[i]
    act=listaOrdenada[i][2]
    pos=i
    while pos> 0 and listaOrdenada[pos-1][2] > act:
        listaOrdenada[pos] = listaOrdenada[pos-1]
        pos=pos-1
    listaOrdenada[pos]=listAux
'''OTRO EJEMPLO DE ORDENAMIENTO QUE SE PUEDE USAR EN PYTHON 3
listaOrdenada = [(c,a,b) for a,b,c in listaOrdenada]
listaOrdenada.sort()
listaOrdenada = [(a,b,c) for c,a,b in listaOrdenada]
'''

#4.- MIENTRAS LA LISTA ORDENADA NO ESTE VACIA, HACER:
while listaOrdenada:
  #5.-TOMAR VERTICE DE LA LISTA ORDENADA Y ELIMINARLO
  print("Toma el vertice de la lista ")
  vertice = listaOrdenada.pop(0)
  d = vertice[1]
  print(d)

  #6.-SI EL DESTINO NO ESTA EN LA LISTA DE VISITADOS
  if d not in listaVisitados:
    print("Si no esta en la lista de visitados se agrega")
    #7.- AGREGAR A LA LISTA DE VISITADOS EN NODO DESTINO
    listaVisitados.append(d)
    #8.- AGREGAR A LA LISTA ORDENADA LOS ADYACENTES DEL NODO DESTINO 
    #"d" QUE NO HAN SIDO VISITADOS
    for key, lista in grafo[d]:
      if key not in listaVisitados:
        listaOrdenada.append((d, key, lista))
    print("Se ordena la lista")
    #####ORDENAMIENTO APLICADO A LA LISTA :
    print(listaOrdenada)
    listaOrdenada = [(c,a,b) for a,b,c in listaOrdenada]
    print("primer ordenamiento")
    print(listaOrdenada)
    listaOrdenada.sort()
    print("segundo ordenamiento")
    print(listaOrdenada)
    listaOrdenada = [(a,b,c) for c,a,b in listaOrdenada]
    print("ultimo ordenamiento")
    print(listaOrdenada)
    #9.-AGREGAR VERTICE AL GRAFO RESULTANTE
    # PARA COMPRENDER MEJOR, EN LAS SIGUIENTES LINEAS SE TOMA EL "VERTICE", QUE EN ESTE CASO
    # ES UNA TUPLA QUE CONTIENE TRES VALORES; EL VERTICE EN SU POSICIÓN 0 ES EL VALOR DEL NODO ORIGEN
    # EL VÉRTICE EN SU POSICIÓN 1 ES EL NODO DESTINO, Y EL VÉRTICE EN SU POSICIÓN 2 ES EL PESO DE LA ARISTA ENTRE AMBOS NODOS,
    # Y A CONTINUACIÓN SE AGREGAN ESOS VALORES AL GRAFO
    origen  = vertice[0]
    destino = vertice[1]
    peso    = vertice[2]

    if origen in grafoResultante:
      if destino in grafoResultante:
        lista = grafoResultante[origen]
        grafoResultante[origen] = lista + [(destino, peso)]
        lista = grafoResultante[destino]
        lista.append((origen, peso))
        grafoResultante[destino] = lista
      else:
        grafoResultante[destino] = [(origen, peso)]
        lista = grafoResultante[origen]
        lista.append((destino, peso))
        grafoResultante[origen] = lista
    elif destino in grafoResultante:
      grafoResultante[origen] = [(destino, peso)]
      lista = grafoResultante [destino]
      lista.append((origen, peso))
      grafoResultante[destino] = lista
    else:
      grafoResultante[destino] = [(origen, peso)]
      grafoResultante[origen] = [(destino, peso)]
      
print("\n\nGrafo resultante:\n")
for key, lista in grafoResultante.items():
  print("Nodo")
  print(key)
  print("Lista a la que enlaza")
  print(lista)