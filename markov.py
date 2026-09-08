from entropia import *
from informacion import *
from fuentes import *


""" multiplico una matriz por un vector"""
def multiplicoMatrizVector(matriz,v):
    n = len(matriz[0])
    v1 = [0] * n
    for j in range(n):
        for i in range(len(v)):
            v1[j] += v[i] * matriz[i][j]
    return v1

"""resto dos vectores"""
def restaVectores(V0,V1):
    return [V0[i] - V1[i] for i in range(len(V0))]

"""ingreso una matriz y una tolerancia y me devuelve el aprox del vector estacionado, si las filas suman 1"""
def calcularValorEstacionario(matriz, tol):
    n = len(matriz)
    V0 = [1 / n for _ in range(n)]
    diferencia = tol + 1  # valor inicial solo para entrar al while
 
    while diferencia > tol:
        V1 = multiplicoMatrizVector(matriz, V0)
        diferencia = max(abs(x) for x in restaVectores(V1, V0))
        V0 = V1  # ahora sí actualizamos la estimación
 
    return V0
 
 


"""
1/2 1/3 0
1/2 1/3 1
0   1/3 0

1/3 1/2 1/6

0.5 0.25 0.25
0.4 0.1 0.5
0.1 0.3 0.6

v0 = 0.3 0.3 0.3
v1 = 0.3 0.3 0.339

v0 = v0 - v1 = 0 0 0.039
max(v0-v1) > 0.01 ->> sigo
v0 = 0 0 0.039
v1 = 0.00975 0.0195 0.0234


"""