from entropia import *
from informacion import *
from fuentes import *

"""Recibe una fila de una matriz de transicion y su nro de columna y devuelve 
si la columna tiene 0s en la mitad inferior correspondiente a la matriz inferior"""
def estaTrianguladaFila(col, j):
    flag = False
    i = 0
    nro = col[i]

    while(not(flag) and i < j):
        flag = nro == 0
        i +=1

    return flag
"""Devuelve si una matriz tiene 0s debajo de la diagonal para el GaussJordan"""
def estaTrianguladaMatriz(matriz):
    flag = False
    i = 1
    col = matriz[i]

    while (not(flag) and i < len(matriz)):
        flag = estaTrianguladaFila(col, i)
        i+=1
    
    return flag

"""intercambio las filas f1 y f2"""
def cambioFilas(f1, f2):
    faux = []
    faux = f2
    f2 = f1
    f1 = faux
    return f1,f2

"""hago el cambio f1 -> f1 + k*f2"""
def combinacionLinFilas(f1,f2, k):
    f2 = [x*k for x in f2] 
    faux = []
    for i in f1:
        faux.append(f1[i]+f2[i])
    return faux

"""divide toda una fila por el pivote P"""
def dividirPivote(fila,p):
    return [x/p for x in fila]


def calcularValorEstacionario(matriz):
    V = []
    
    
    
    return V

"""
1/2 1/3 0
1/2 1/3 1
0   1/3 0

1/3 1/2 1/6
"""