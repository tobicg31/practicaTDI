"""
Dada el siguiente mensaje emitido por una fuente de información:
Obtener la matriz de transición de la fuente
Determinar si se trata de una fuente de memoria nula o con memoria
Generar la extensión de orden 2 a partir de su distribución estacionaria
Calcular la entropía de la fuente y de la extensión obtenida
devuelveProbabilidad

"""
from math import *
def cantApariciones(c, mensaje):
    cant = 0
    for i in range(len(mensaje)):
        cant += c == mensaje[i]
    return cant


def devuelveProbabilidad(mensaje, alf):
    """Devuelve las probabilidades de cada símbolo, en el mismo orden que alf"""
    return [cantApariciones(simbolo, mensaje) / len(mensaje) for simbolo in alf]
"""Dado un mensaje y su alfabeto, devuelve la matriz de transicion del msg
   matriz[i][j] = P(alf[i] | alf[j]): columna = origen, fila = destino"""
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
                if ((mensaje[pos2]== alf[k]) and (mensaje[pos1]==alf[i]) ):
                    matriz[k][i]+=1
                pos1+=1
                pos2+=1

    for i in range(len(alf)):
            for k in range(len(alf)):
                matriz[k][i] /= cantApariciones(alf[i],mensaje[:-1])
    return matriz

def esFuenteMemoriaNula(matriz, tol):
    filas = len(matriz)
    columnas = len(matriz[0])
    primera = [matriz[f][0] for f in range(filas)]

    for c in range(1, columnas):
        for f in range(filas):
            if abs(matriz[f][c] - primera[f]) > tol:
                return False
    return True
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

"""recibo un alfabeto, sus probabilidades y n, devuelvo la extension de orden n y sus probabilidades """
def ExtensionOrdenN(alfabeto, probabilidades, N):
    ext = []
    prob = []
    if N==1:
        ext = alfabeto
        prob = probabilidades
    else:
        extN1, probN1 = ExtensionOrdenN(alfabeto, probabilidades, N-1)
        for i in range(len(alfabeto)):
            for j in range(len(extN1)):
                ext.append(alfabeto[i] + str(extN1[j]))
                prob.append(probabilidades[i] * probN1[j])
    return ext, prob
def EntropiaMarkov(vec,m):
    H = 0
    n = len(m)
    for i in range(n):
        suma = 0
        for j in range(n):
            if m[j][i] >0:
                suma += m[j][i]*log2(1/m[j][i])
        H += vec[i] * suma
    return H


if (__name__ == "__main__"):
    mensaje = "CCAABBCCAABBCCAABBCCAABBCCAABB"
    print(len(mensaje))
    alf = ["A","B","C"]
    prob = devuelveProbabilidad(mensaje, alf)
    print(prob)
    matriz = calcularMatrizTransicion(mensaje, alf)
    for i in matriz:
        print(i)

    

    print("es memoria nula?: ",esFuenteMemoriaNula(matriz, 0.000000000000001))

    vec = calcularValorEstacionario(matriz, 0.00000000000001)
    print("vector estacionario: ",vec)
    extension2, prob2 = ExtensionOrdenN(alf, vec, 2)
    print(extension2)
    print(prob2)

    print("entropia H2(S): ", EntropiaMarkov(vec, matriz))
    print("entropia H2(S^2)", 2*EntropiaMarkov(vec, matriz))
