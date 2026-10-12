from entropia import *
from markov import *
from codificacion import *
from fuentes import *


def cumpleTeoremaShannon(prob, palabrasN, N):
    alf = devuelveAlfabetoCodigo(palabrasN)

    HS = entropiaBaseR(prob, len(alf))
    print(HS)

    probN = probabilidadesOrdenN(prob, 2)

    Ln = longitudMedia(longitudesCodigo(palabrasN), probN)
    print(Ln)

    return (Ln/N >= HS) and (Ln/N < (HS + 1/N))