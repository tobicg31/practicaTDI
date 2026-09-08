from entropia import *
from informacion import *
from fuentes import *
from random import *


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

def cantApariciones(c, mensaje):
    cant=0
    for i in range(len(mensaje)):
        cant += c==mensaje[i]
    return cant

"""Dado un mensaje y su alfabeto, devuelve la matriz de transicion del msg"""
def calcularMatrizTransicion(mensaje,alf):
    n = len(alf)
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)

    for i in range(n): 
        for k in range(n):
            pos1 = 0
            pos2 = 1
            while (pos2 < len(mensaje)):
                if ((mensaje[pos2]== mensaje[k]) and (mensaje[pos1]==mensaje[i]) ):
                    matriz[k][i]+=1
                pos1+=1
                pos2+=1

    for i in range(len(alf)):
            for k in range(len(alf)):
                matriz[k][i] /= cantApariciones(alf[i],mensaje)
    return matriz

def probAcumuladaColumna(prob,i):
    acum = []
    acum.append(prob[0][i])
    for k in range(1,len(prob)):
        acum.append(acum[k-1]+prob[k][i])
    return acum

def devuelvecadenadimensionN(n,alf,m):
    msj= ""
    msj+= alf[1] #vector estacionado
    sigcol=1
    for i in range(2,n):
        col = [m[f][sigcol] for f in range(len(m))]
        Acum = probAcumulada(col)
        print(f"columna y acum: {col, Acum}")
        r = random()
        sigcol =buscoAcum(Acum,r)
        msj += alf[sigcol]
    return msj
        
        
        


"""
acacbcbc
"""
 
 


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