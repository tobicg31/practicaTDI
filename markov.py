from entropia import *
from informacion import *
from fuentes import *

def multiplicoMatrizVector(matriz,v):
    v1 =[]
    for i in range(len(v)):
        v1.append(0)

    for i in range(len(v)):
        for k in range(len(matriz)):
            v1[i] += matriz[i][k]*v[k]
    return v1

def restaVectores(V0,V1):
    return [V0[i] - V1[i] for i in range(len(V0))]

def calcularValorEstacionario(matriz, tol):
    V0 = []
    for i in range(len(matriz)):
        V0.append(1/len(matriz))

    while max(V0) > tol:
        #V1 = multiplicoMatrizVector(matriz, V0)
        V1 = V0*matriz
        V0 = restaVectores(V0,V1)
        

    return V0
"""
1/2 1/3 0
1/2 1/3 1
0   1/3 0

1/3 1/2 1/6
"""