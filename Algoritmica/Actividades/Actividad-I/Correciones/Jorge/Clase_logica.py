
class ecuacion:
    def __init__(self,A,B,C,D,F,G):
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        self.F=F
        self.G=G

    def comprobarEcuacion(self):
        iguales=True
        numero=(int(0))

        for i in range(0,2):
            for j in range(0,2):
                self.F[numero]=not(self.A[i] and self.B[j] or self.F[i] and self.G[j])
                self.G[numero]=not(self.A[i] and self.B[j]) and not(self.F[i] and self.G[j])
                numero=numero+1

        for i in range(0,numero):
            if(self.F[i]!=self.G[i]):
                iguales=False
                exit

        if(iguales):
            return "Se cumple la ecuacion logica"
        else:
            return "No se cumple la ecuacion logica"
