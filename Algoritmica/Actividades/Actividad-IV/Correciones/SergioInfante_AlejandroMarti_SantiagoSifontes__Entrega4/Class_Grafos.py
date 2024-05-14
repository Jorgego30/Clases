import sys
import os

class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.color ='skyblue'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion
    
    def __str__(self):
        return str(self.id) + \
            ":color " + self.color + \
                ":disc " + str(self.disc) + \
                ":fin " + str(self.fin) + \
                    ":dist " + str(self.dist) + \
                    ":pred [" + str(self.pred)+ "]\n\t" + \
                    ' conectadoA: ' + str([x.id for x in self.conectadoA])
    
    def asignarColor(self,color):
        self.color = color
        
    def asignarDistancia(self,d):
        self.dist = d

    def asignarPredecesor(self,p):
        self.pred = p

    def asignarDescubrimiento(self,dtime):
        self.disc = dtime
        
    def asignarFinalizacion(self,ftime):
        self.fin = ftime
        
    def obtenerFinalizacion(self):
        return self.fin
        
    def obtenerDescubrimiento(self):
        return self.disc
        
    def obtenerPredecesor(self):
        return self.pred
        
    def obtenerDistancia(self):
        return self.dist
        
    def obtenerColor(self):
        return self.color

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
    
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()
    

    def Graph2Table(self):
        Tabla = []
        for i in self.obtenerVertices():
            for j in self.listaVertices[i].conectadoA.keys():
                origen = i
                destino = j.id
                peso = self.listaVertices[i].conectadoA[j]
                Tabla.append([origen, destino, peso])
        return Tabla

            


    def __iter__(self):
        return iter(self.listaVertices.values())



