class TablaHash:
    def __init__(self): #constructor
        self.tamano = 11
        self.slots = [None] * self.tamano
        self.datos = [None] * self.tamano
        self.size = 0
       
        

    def agregar(self, clave, dato): #definimos la función para añadir elementos

        valorHash = self.funcionHash(clave, len(self.slots))

        if self.slots[valorHash] == None:
            self.slots[valorHash] = clave
            self.datos[valorHash] = dato
            self.size += 1
        else:
            if self.slots[valorHash] == clave:
                self.datos[valorHash] = dato  # reemplazo
            else:
                proximaSlot = self.rehash(valorHash, len(self.slots))
                while self.slots[proximaSlot] != None and self.slots[proximaSlot] != clave:
                    proximaSlot = self.rehash(proximaSlot, len(self.slots))

                if self.slots[proximaSlot] == None:
                    self.slots[proximaSlot] = clave
                    self.datos[proximaSlot] = dato
                    self.size += 1
                else:
                    self.datos[proximaSlot] = dato  # reemplazo

    def funcionHash(self, clave, tamano): #en esta funcion miramos que posición debe ocupar el elemento
        
        return clave % tamano

    def rehash(self, hashViejo, tamano): #en esta funcion miramos que posición debe ocupar el elemento al 
        return (hashViejo+1) % tamano

    def obtener(self, clave): # definimos la función para obtener el dato de una clave
        slotInicio = self.funcionHash(clave, len(self.slots)) 

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        while self.slots[posicion] != None and not encontrado and not parar:
            if self.slots[posicion] == clave:
                encontrado = True
                dato = self.datos[posicion]
            else:
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
        return dato

    def agrandista(self):  # definimos la función para agrandar la tabla cuando se llega al 90% de le capacidad 
        old_tam=self.tamano
        tamano=self.tamano*2
        self.tamano=self.primos(tamano)
        new_tam=self.tamano
        self.slots=self.slots+([None]*(new_tam-old_tam))
        self.datos=self.datos+([None]*(new_tam-old_tam))
        self.organizador()

    def organizador(self): #definimos la función para organizar la tabla
        for i in range(self.tamano):
            if self.slots[i]!=None:
                clave=self.slots[i]
                dato=self.datos[i]
                self.slots[i]=None
                self.datos[i]=None
                self.size=self.size-1
                self.agregar(clave,dato)

    def porcentage(self): #en esta función se calcula el porcentage de carga
        percent=float
        percent=self.size/self.tamano
        
        return percent
    
    def primos(self,n): #esta función es simplemente para tener todos los num primos
        primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        for i in primos:

            if i > n:
                return i
        return None

    def borrar(self,clave): #definimos la función para borrar un elemento
        slotInicio = self.funcionHash(clave, len(self.slots))

        dato = None
        parar = False
        encontrado = False
        posicion = slotInicio
        while self.slots[posicion] != None and not encontrado and not parar:
            if self.slots[posicion] == clave:
                encontrado = True
                self.datos[posicion]=None
                self.slots[posicion]=None
            else:
                posicion = self.rehash(posicion, len(self.slots))
                if posicion == slotInicio:
                    parar = True
        
        


    def __getitem__(self, clave): # definimos la función para obtener el dato de una clave
        return self.obtener(clave)

    def __setitem__(self, clave, dato):   # definimos la función para agregar un elemento
       
        porrocentage=self.porcentage()
        if porrocentage>=0.9:
            self.agrandista()
        else:
            pass

        self.agregar(clave, dato)
   
    def __len__(self): # definimos la función para obtener el tamaño de la tabla
        return self.size