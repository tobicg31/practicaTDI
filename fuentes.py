from informacion import *
from entropia import *
from math import *

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

def probabilidadesOrdenN(probabilidades, N):
    if N == 1:
        return list(probabilidades)

    prob = []
    prob1 = probabilidadesOrdenN(probabilidades, N - 1)
    for i in range(len(probabilidades)):
        for j in range(len(prob1)):
            prob.append(probabilidades[i] * prob1[j])
    return prob