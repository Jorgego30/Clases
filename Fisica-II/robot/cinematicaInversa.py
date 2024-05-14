from lecturaRobot import *
import numpy as np
import sympy as sp
import optparse

desc="Resolucion del problema cinematico inverso para el Robot Niryo One."

global ids
global numberOfIds
global q
global w

ids, q, w = leer()
numberOfIds = len(ids)

# convierte un eje de rotacion en una matriz antisimetrica 3x3
def VecToso3(w): 
    return np.array([[0,-w[2],w[1]], [w[2],0,-w[0]], [-w[1],w[0],0]])

# convierte un vector giro o eje helicoidal en matriz 4x4 se3
def VecTose3(V): 
    return np.r_[np.c_[VecToso3([V[0], V[1], V[2]]), [V[3], V[4], V[5]]], np.zeros((1, 4))]

# extrae un vector de 3 componentes de una matriz antisimetrica so3
def so3ToVec(so3mat): 
    return np.array([so3mat[2][1], so3mat[0][2], so3mat[1][0]])

# Convierte una matriz se3 en un vector giro 1x6
def se3ToVec(se3mat): 
    return np.r_[[se3mat[2][1], se3mat[0][2], se3mat[1][0]], [se3mat[0][3], se3mat[1][3], se3mat[2][3]]]

# Formula de Rodrigues para obtener matriz de Rotacion
def getR(w,ang): 
    wmat=VecToso3(w)
    return np.eye(3)+np.sin(ang)*wmat+(1.-np.cos(ang))*np.dot(wmat,wmat)

def getT(orientation,r): # Devuelve la matriz de transformaci´on homog´enea
    i=np.array([1,0,0]); j=np.array([0,1,0]); k=np.array([0,0,1])
    Ri=getR(i,orientation[0]); Rj=getR(j,orientation[1]); Rk=getR(k,orientation[2])
    R=np.matmul(Rk,np.matmul(Rj,Ri))
    aux=np.array([[0,0,0,1]])
    return np.r_[np.c_[R,r],aux]

def getS(): # Devuelve los ejes helicoidales del robot Niryo One en la posici´on cero
    # Definimos los eslabones
    scalefactor=0.001 # por si quiero los resultados en otras unidades
    L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])*scalefactor
    # Calculamos los ejes de giro y vectores posici´on en la configuraci´on final del robot
    qs=[]; ws=[]
    qs.append(np.array(q[0]))
    ws.append(np.array(w[0]))
    for i in range(1,numberOfIds,1):
        ws.append(np.array(w[i]))
        qs.append(np.array(q[i])+qs[i-1])
    # Calculamos las velocidades lineales para construir los ejes helicoidales
    vs=[]; Si=[]
    for i in range(0,numberOfIds,1):
        vs.append(np.cross(qs[i],ws[i]))
        Si.append(np.r_[ws[i],vs[i]])
    return Si

def MatrixExp6(se3mat): # convierte un vector giro en forma matricial 4x4 se3 en una MTH a trav´es de la exponencial
    se3mat = np.array(se3mat) # vector giro en representaci´on matricial se3 (4x4)
    v=se3mat[0: 3, 3] # extraemos el vector v*theta (velocidad lineal)
    omgmattheta=se3mat[0: 3, 0: 3] # extraemos omega*theta en forma matricial 3x3 (so3)
    omgtheta = so3ToVec(omgmattheta) # lo pasamos a forma vectorial
    if (np.linalg.norm(omgtheta))<1.e-6: # en el caso de que no haya giro (omega despreciable)
        return np.r_[np.c_[np.eye(3), v], [[0, 0, 0, 1]]] # concatena columnas y filas. S´olo traslaci´on
    else: # caso general
        theta = np.linalg.norm(omgtheta)
        omgmat = omgmattheta / theta # omega en forma matricial 3x3 (so3) Normalizada
        # a continuaci´on aplicamos la definici´on de matriz exponencial que vimos en clase (slide 42, tema 2)
        G_theta=np.eye(3)*theta+(1-np.cos(theta))*omgmat+(theta-np.sin(theta))*np.dot(omgmat,omgmat)
        R=np.eye(3)+np.sin(theta)*omgmat+(1.-np.cos(theta))*np.dot(omgmat,omgmat)
        return np.r_[np.c_[R,np.dot(G_theta,v)/theta],[[0, 0, 0, 1]]]

def MatrixLog3(R): # Calcula la matriz logaritmo de una matriz de rotaci´on
    acosinput = (np.trace(R) - 1) *0.5
    if np.trace(R) >= 3: return np.zeros((3, 3))
    elif np.trace(R) <= -1:
        if abs(1 + R[2][2])>1.e-6: omg = (1.0 / np.sqrt(2 * (1 + R[2][2]))) * np.array([R[0][2], R[1][2], 1 + R[2][2]])
        elif abs(1 + R[1][1])>1.e-6: omg = (1.0 / np.sqrt(2 * (1 + R[1][1]))) * np.array([R[0][1], 1 + R[1][1], R[2][1]])
        else: omg = (1.0 / np.sqrt(2 * (1 + R[0][0]))) * np.array([1 + R[0][0], R[1][0], R[2][0]])
        return VecToso3(np.pi * omg)
    else:
        theta = np.arccos(acosinput)
        return (theta*0.5)/np.sin(theta) * (R-np.array(R).T)

def MatrixLog6(T): # Calcula la matriz logaritmo de una MTH
    R=T[0: 3, 0: 3]; p = T[0: 3, 3] # separa la MTH en matriz de rotaci´on y vector traslaci´on
    omgmat = MatrixLog3(R) # coordenadas exponenciales de la matriz de rotaci´on
    # o sea, un vector de rotaci´on como matriz antisim´etrica so3 (3x3)
    if np.array_equal(omgmat, np.zeros((3, 3))): # Si no hay rotaci´on, es una matriz de ceros
        return np.r_[np.c_[np.zeros((3, 3)),p],[[0, 0, 0, 0]]]
    else:
        omgvec= so3ToVec(omgmat) # expresa la rotaci´on como un vector en la direcci´on del eje por el ´angulo
        omgmat=omgmat/np.linalg.norm(omgvec) # el vector en el eje de rotaci´on normalizado y en forma matricial
        theta = np.linalg.norm(omgvec) # tambi´en se puede calcular como np.arccos((np.trace(R)-1)/2.0)
        # a continuaci´on aplicamos la definici´on que vimos en clase (ver diapositivas)
        invG_theta=np.eye(3)/theta-omgmat*0.5+(1.0/theta-0.5/np.tan(theta*0.5))*np.dot(omgmat,omgmat)
        v=np.dot(invG_theta,p)
        return np.r_[np.c_[omgmat,v],[[0, 0, 0, 0]]]*theta # primero concatena columnas y luego filas

def Adjunta(T): # Calcula la matriz adjunta de una MTH
    R=T[0: 3, 0: 3]; p = T[0: 3, 3]
    return np.r_[np.c_[R, np.zeros((3, 3))], np.c_[np.dot(VecToso3(p), R), R]]

def CinematicaDirecta(M,S,t):
    T=np.eye(4)
    for i in range(0,numberOfIds,1): 
        T=np.dot(T,MatrixExp6(VecTose3(S[i]*t[i])))
        return np.dot(T,M)

def Jacobiana(theta):
    w=getejes() # Definimos ejes de rotaci´on
    q=getqs() # Definimos vectores q
    # Definimos los eslabones
    scalefactor=0.001 # por si quiero los resultados en otras unidades
    L=np.array([103.0, 80.0, 210.0, 30.0, 41.5, 180.0, 23.7, -5.5])*scalefactor
    t=sp.symbols("t0, t1, t2, t3, t4, t5, t6") #Coordenadas de las articulaciones
    # Calculamos las matrices de rotaci´on a partir de los ejes w, utilizando la f´ormula de Rodrigues
    R=[]
    for i in range(0,numberOfIds,1):
        wmat=sp.Matrix(VecToso3(w[i]))
        R.append(sp.eye(3)+sp.sin(t[i])*wmat+(1-sp.cos(t[i]))*(wmat*wmat))
    # Aplicamos rotaciones a los vectores q y w para llevarlos a la configuraci´on del robot que queremos
    qs=[]; ws=[]; Ri=R[0]
    qs.append(sp.Matrix(q[0]))
    ws.append(sp.Matrix(w[0]))
    for i in range(1,numberOfIds,1):
        ws.append(Ri*sp.Matrix(w[i]))
        qs.append(Ri*sp.Matrix(q[i])+qs[i-1])
        Ri=Ri*R[i]
    # Calculamos las velocidades lineales, los vectores giro correspondientes y la matriz Jacobiana
    vs=[]; Ji=[]; i=0
    vs.append(qs[i].cross(ws[i]))
    Ji.append(ws[i].row_insert(3,vs[i]))
    J=Ji[0]
    for i in range(1,numberOfIds,1):
        vs.append(qs[i].cross(ws[i]))
        Ji.append(ws[i].row_insert(3,vs[i]))
        J=J.col_insert(i,Ji[i])
    return np.array(J.subs({t[0]:theta[0], t[1]:theta[1], t[2]:theta[2], t[3]:theta[3], t[4]:theta[4]}))



def main():

    parser = optparse.OptionParser(description=desc, version="%prog version 1.0")
    parser.add_option("-j", "--seed_joints", help="Coordenadas iniciales de las articulaciones en rad", action="store")
    parser.add_option("-r", "--xyz", help="Coordenadas xyz finales para el elemento terminal", action="store")
    parser.add_option("-a", "--ang", help="´Angulos de Euler finales para el elemento terminal en grados", action="store")
    parser.add_option("-o", "--eomg", help="Error en la orientaci´on del elemento terminal (0.01 por defecto)", action="store")
    parser.add_option("-e", "--er", help="Error en la posici´on del elemento terminal (0.001 por defecto)", action="store")
    parser.set_defaults(seed_joints="0 0 0 0 0 0 0", xyz="0 0 0", ang="0 0 0", eomg="0.01", ev="0.001")
    options, arguments = parser.parse_args()

#**************************************************************************************

    seed_joints=str(options.seed_joints).split()
    t=[]
    for i in range (0,6,1): t.append(float(seed_joints[i]))

    xyz=str(options.xyz).split()
    r=[]
    for i in range (0,3,1): r.append(float(xyz[i]))

    ang=str(options.ang).split()
    orientation=[]
    for i in range (0,3,1): orientation.append(np.deg2rad(float(ang[i])))

    eomg=float(options.eomg)
    ev=float(options.ev)

    scalefactor=0.001
    L=np.array([50, 50, 100, 50, 100, 50, 70]) * scalefactor

    # Calculamos la Matriz de Transformaci´on Homog´enea a partir de posiciones y ´angulos
    T=getT(orientation, r)

    #print(np.round(T,2))
    # Calculamos los ejes helicoidales en la posici´on cero del robot
    S=getS()
    #print(S)
    # Matriz de transformaci´on homog´enea en la posici´on cero del robot
    M=np.array([[1,0,0,0],[0,1,0,L[2]+L[3]+L[4]+L[5]+L[6]],[0,0,1,L[0]+L[1]],[0,0,0,1]])

    thetalist = np.array(t).copy()
    i = 0
    maxiterations = 20
    Tsb = CinematicaDirecta(M,S, thetalist) # Resuelve la Cinem´atica Directa para thetalist

    
    Vb = MatrixLog6(np.dot(np.linalg.inv(Tsb), T)) # vector Giro para ir a la posici´on deseada en {b}
    Vs = np.dot(Adjunta(Tsb), se3ToVec(Vb)) # vector Giro en el SR de la base {s}
    


"""
    # condici´on de convergencia: m´odulo de velocidad angular < eomg y velocidad lineal < ev
    err = np.linalg.norm([Vs[0], Vs[1], Vs[2]]) > eomg or np.linalg.norm([Vs[3], Vs[4], Vs[5]]) > ev

    while err and i < maxiterations:
        J=Jacobiana(thetalist)
        J=np.array(J.tolist()).astype(np.float64)
        thetalist = thetalist + np.dot(np.linalg.pinv(J), Vs)
        
        while thetalist[0] < -3.053:
            thetalist[0]=thetalist[0]+1/2*np.pi
        while thetalist[0] > 3.053:
            thetalist[0]=thetalist[0]-1/2*np.pi

        while thetalist[1] < -1.919:
            thetalist[1]=thetalist[1]+1/2*np.pi
        while thetalist[1] > 0.639:
            thetalist[1]=thetalist[1]-1/2*np.pi

        while thetalist[2] < -1.396:
            thetalist[2]=thetalist[2]+1/2*np.pi
        while thetalist[2] > 1.57:
            thetalist[2]=thetalist[2]-1/2*np.pi

        while thetalist[3] < -3.053:
            thetalist[3]=thetalist[3]+1/2*np.pi
        while thetalist[3] > 3.053:
            thetalist[3]=thetalist[3]-1/2*np.pi

        while thetalist[4] < -1.744:
            thetalist[4]=thetalist[4]+1/2*np.pi
        while thetalist[4] > 1.919:
            thetalist[4]=thetalist[4]-1/2*np.pi

        while thetalist[5] < -2.573:
            thetalist[5]=thetalist[5]+1/2*np.pi
        while thetalist[5] > 2.573:
            thetalist[5]=thetalist[5]-1/2*np.pi

        #print(thetalist,"\n")
        i = i + 1
        Tsb = CinematicaDirecta(M, S, thetalist)
        Vb = MatrixLog6(np.dot(np.linalg.inv(Tsb), T))
        Vs = np.dot(Adjunta(Tsb), se3ToVec(Vb)); print (Vs)
        err = np.linalg.norm([Vs[0], Vs[1], Vs[2]]) > eomg or np.linalg.norm([Vs[3], Vs[4], Vs[5]]) > ev
    

    

    print ("\n\nCoordenadas de las articulaciones:\n", thetalist)
    print ("Error en w:", np.round(np.linalg.norm([Vs[0], Vs[1], Vs[2]]),8))
    print ("Error en v:", np.round(np.linalg.norm([Vs[3], Vs[4], Vs[5]]),8))
    print ("N´umero de iteraciones:", i)
"""

if __name__=="__main__" :
   main()
