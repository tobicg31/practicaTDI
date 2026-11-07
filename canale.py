from markov import *
from entropia import *

def MatrizPba(alfE, alfS,entrada, salida):
    """
    le paso alfabetos y los msg de entrada y salida y devuelve
    la matriz del canal P(bj/ai)
    """
    aparicionesE = [cantApariciones(i, entrada) for i in alfE]
    aparicionesS = [cantApariciones(i, salida) for i in alfS]
    matriz = []
    for i in range(len(aparicionesE)):
        matriz.append([])
        for j in range(len(aparicionesS)):
            matriz[i].append(0) 

    for c in range(len(alfE)):
        for i in range(len(entrada)):
            if entrada[i]==alfE[c]:
                matriz[c][int(salida[i])] +=1
        for i in range(len(alfS)):
            matriz[c][i] /= aparicionesE[c]

    return matriz

def probSalida(matriz, probPriori):
    """
    le paso la matriz del canal y las probabilidades a priori P(ai)
    y devuelve las probabilidades de salida P(bj)
    """
    pSalida = []
    for i in range(len(matriz[1])):
        pSalida.append(0)

    for k in range(len(matriz[1])):
        for i in range(len(probPriori)):
            pSalida[k] += probPriori[i]*matriz[i][k]
    
    return pSalida

def probPosteriori(matriz, priori, salida):
    """
    le paso la matriz de canal, P(ai), P(bj)
    y devuelve las probabilidades a posteriori P(ai/bj)
    """
    poste = []
    for i in range(len(matriz)):
        poste.append([])
        for j in range(len(matriz[1])):
            poste[i].append((matriz[i][j]*priori[i])/salida[j]) 
    return (poste)

def probSimultaneos(matriz, salida):
    """
    le paso la matriz del canal y P(bj)
    y devuelve las probabilidades simultaneas P(ai, bj)
    """
    simul = []
    for i in range(len(matriz)):
        simul.append([])
        for j in range(len(matriz[1])):
            simul[i].append((matriz[i][j])*salida[j]) 

    return (simul)

def entropiaPriori(priori):
    """
    le paso las prob a priori P(ai)
    y devuelve su entropia H(A)
    """
    return Entropia(priori, listaInformacion(priori))

def entropiaPosteriori(priori, matriz):
    """
    le paso las prob a priori P(ai) y la matriz del canal
    y devuelve las entropias a posteriori H(A/bj)
    """
    Hpost = [] 
    salida = probSalida(matriz, priori)
    posteriori = probPosteriori(matriz, priori, salida)
    for i in range(len(salida)):
        col = []
        for k in range(len(priori)):
            col.append(posteriori[k][i])
        Hpost.append(entropiaPriori(col))
    return Hpost

def equivocacion(salida, Hpost):
    """
    le paso las prob de salida P(bj) y la entropia a post H(A/bj)
    y devuelve la equivocacion/ruido H(A/B)
    """
    equi = 0
    for i in range(len(salida)):
        equi+= salida[i]*Hpost[i]
    return equi

def perdida(equi, Hpriori, Hsalida):
    """
    le paso la equivocacion H(A/B), las entropias a priori H(A) y de salida H(B)
    y devuelve la perdida H(B/A)
    """
    return equi + Hsalida - Hpriori

def entropiaAfin(Ha, Hba):
    """
    le paso la entropia a priori H(A) y la perdida
    y devuelve la entropia conjunta/afin H(A,B)
    """
    return Ha+Hba

def informacionMutua(Hb, Hba):
    """
    le paso la entropia de salida H(B) y la perdida
    y devuelve la inform mututa I(A, B)
    
    """
    return Hb-Hba

def esSinRuido(matriz):
    """
    le paso una matriz y devuelve si es sin ruido o no
    revisa si hay mas de un elemento != 0 por columna
    """
    cont = []
    for k in range(len(matriz[1])):
        cont.append(0)

    for j in range(len(matriz[1])):
        for i in range(len(matriz)):
            if matriz[i][j] > 0:
                cont[j] += 1

    k =0
    bool = False
    while (k <len(cont)) and not(bool) :
        bool = cont[k]>1
        k+=1
    return not(bool)

def esDeterminante(matriz):
    """
    le paso una matriz y devuelve si es determinante o no
    revisa si hay mas de un elemento != 0 por fila
    """
    cont = []
    for k in range(len(matriz)):
        cont.append(0)

    for i in range(len(matriz)):
        for j in range(len(matriz[1])):
            if matriz[i][j] > 0:
                cont[i] += 1

    k =0
    bool = False
    while (k <len(cont)) and not(bool) :
        bool = cont[k]>1
        k+=1
    return not(bool)

def matrizCompuesto(a, b):
    """
    le paso dos matrices y las multiplica basically
    """
    prod = []
    for i in range(len(a)):
        prod.append([])
        for j in range(len(b[1])):
            prod[i].append(0.0) 

    for i in range(len(a)):
        for j in range(len(b[1])):
            for k in range(len(b)):
                prod[i][j] += a[i][k] * b[k][j]
    return prod

def capacidadDet(matriz):
    """
    capacidad si es det, log(nro salidas)
    """
    return log(len(matriz[1]))

def capacidadSinRuido(matriz):
    """
    capacidad si es sin ruido, log(nro entradas)
    """
    return log(len(matriz))