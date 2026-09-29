from entropia import *
from informacion import *
from fuentes import *
from random import *

# Convencion de la matriz de transicion:
#   matriz[i][j] = P(alf[i] | alf[j])
#   columna j = simbolo de ORIGEN, fila i = simbolo de DESTINO
#   cada COLUMNA suma 1 (matriz estocastica por columnas)
# Los indices siguen el orden del alfabeto (alf ordenado).
def devuelveProbabilidad(mensaje, alf):
    """Devuelve las probabilidades de cada símbolo, en el mismo orden que alf"""
    return [cantApariciones(simbolo, mensaje) / len(mensaje) for simbolo in alf]

"""multiplico una matriz por un vector: devuelve M * v (v de largo n)"""
def multiplicoMatrizVector(matriz, v):
    n = len(matriz)
    v1 = [0] * n
    for i in range(n):
        for j in range(len(v)):
            v1[i] += matriz[i][j] * v[j]
    return v1

"""resto dos vectores"""
def restaVectores(V0, V1):
    return [V0[i] - V1[i] for i in range(len(V0))]

"""ingreso una matriz y una tolerancia y me devuelve el aprox del vector estacionario, si las columnas suman 1"""
def calcularValorEstacionario(matriz, tol):
    n = len(matriz)
    V0 = [1 / n for _ in range(n)]
    diferencia = tol + 1  # valor inicial solo para entrar al while

    while diferencia > tol:
        V1 = multiplicoMatrizVector(matriz, V0)
        diferencia = max(abs(x) for x in restaVectores(V1, V0))
        V0 = V1

    return V0

def cantApariciones(c, mensaje):
    cant = 0
    for i in range(len(mensaje)):
        cant += c == mensaje[i]
    return cant


"""Dado un mensaje y su alfabeto, devuelve la matriz de transicion del msg
   matriz[i][j] = P(alf[i] | alf[j]): columna = origen, fila = destino"""
def calcularMatrizTransicion(mensaje, alf):
    n = len(alf)
    indice = {simbolo: pos for pos, simbolo in enumerate(alf)}

    # matriz[destino][origen] = cantidad de veces que alf[destino] sigue a alf[origen]
    matriz = [[0] * n for _ in range(n)]

    for pos in range(len(mensaje) - 1):
        origen = indice[mensaje[pos]]
        destino = indice[mensaje[pos + 1]]
        matriz[destino][origen] += 1

    # Normalizar cada columna (el total coincide con cantApariciones(alf[j], mensaje[:-1]))
    for j in range(n):
        total = sum(matriz[i][j] for i in range(n))
        if total > 0:
            for i in range(n):
                matriz[i][j] /= total

    return matriz

def probAcumuladaColumna(prob, i):
    acum = []
    acum.append(prob[0][i])
    for k in range(1, len(prob)):
        acum.append(acum[k-1] + prob[k][i])
    return acum

def devuelvecadenadimensionN(n, alf, m):
    msj = ""
    msj += alf[1]  # vector estacionario
    sigcol = 1
    for i in range(1, n):
        col = [m[f][sigcol] for f in range(len(m))]
        Acum = probAcumulada(col)
        r = random()
        sigcol = buscoAcum(Acum, r)
        msj += alf[sigcol]
    return msj

def esFuenteMemoriaNula(matriz, tol):
    filas = len(matriz)
    columnas = len(matriz[0])
    primera = [matriz[f][0] for f in range(filas)]

    for c in range(1, columnas):
        for f in range(filas):
            if abs(matriz[f][c] - primera[f]) > tol:
                return False
    return True

