class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i//2]:
            #los intercambio
             self.listaMonticulo[i//2],self.listaMonticulo[i] = self.listaMonticulo[i],self.listaMonticulo[i//2]
          i = i // 2

    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
            #los intercambio
            self.listaMonticulo[i],self.listaMonticulo[hm] = self.listaMonticulo[hm],self.listaMonticulo[i]
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1


#=====================================================================================================
class ColaPrioridad():
    def __init__(self):
       self.MB = MonticuloBinario()

    def avanzar(self):
       return self.eliminarMin()
    
    def agregar(self,elemento):
       self.MB.insertar(elemento)


#============================================================

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.MB.tamanoActual = len(unaLista)
      self.MB.listaMonticulo += unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

    def infiltAbajo(self,i):
      while (i * 2) <= self.MB.tamanoActual:
          hm = self.hijoMin(i)
          if self.MB.listaMonticulo[i][1].id > self.MB.listaMonticulo[hm][1].id:
            #los intercambio (Las tuplas, no los ID de los vertices )
            self.MB.listaMonticulo[i],self.MB.listaMonticulo[hm] = self.MB.listaMonticulo[hm],self.MB.listaMonticulo[i]
          i = hm

    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.MB.listaMonticulo[i][1].id < self.MB.listaMonticulo[i//2][1].id:
            #los intercambio
             self.MB.listaMonticulo[i//2][1],self.MB.listaMonticulo[i][1] = self.MB.listaMonticulo[i][1],self.MB.listaMonticulo[i//2][1]
          i = i // 2

    def hijoMin(self,i):
      if i * 2 + 1 > self.MB.tamanoActual:
          return i * 2
      else:
          # Accedemos al segundo valor que es un vertice y a su vez al nº
          if self.MB.listaMonticulo[i*2][1].id < self.MB.listaMonticulo[i*2+1][1].id:
              return i * 2
          else:
              return i * 2 + 1
          
    def eliminarMin(self):
      valorSacado = self.MB.listaMonticulo[1]
      self.MB.listaMonticulo[1] = self.MB.listaMonticulo[self.MB.tamanoActual]
      self.MB.tamanoActual = self.MB.tamanoActual - 1
      self.MB.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado
          
#============================================================


    def decrementarClave(self,NextVert,NDist): 
        done = False
        i = 1
        myKey = 0
        while not done and i <= self.MB.tamanoActual:
            if self.MB.listaMonticulo[i][1] == NextVert:
                done = True
                myKey = i
            else:
                i += 1
        if myKey > 0:
            self.MB.listaMonticulo[myKey] = (NDist,self.MB.listaMonticulo[myKey][1])
            self.infiltArriba(myKey)
     
    '''
    Priority Queque:
    def decreaseKey(self,val,amt):
            done = False
            i = 1
            myKey = 0
            while not done and i <= self.currentSize:
                if self.heapArray[i][1] == val:
                    done = True
                    myKey = i
                else:
                    i = i + 1
            if myKey > 0:
                self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
                self.percUp(myKey)
    '''
       

    def estaVacia(self):
       return self.MB.tamanoActual == 0

    def __str__(self):
       ListaMonticulo = self.MB.listaMonticulo[1:]
       StringResult = ''
       for i in ListaMonticulo:
          StringResult += str(i)
          
       return StringResult
       
#=====================================================================================================