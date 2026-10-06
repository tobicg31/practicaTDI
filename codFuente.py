from entropia import *
from markov import *
from codificacion import *


def cumpleTeoremaShannon(prob, palabrasN, N):
    alf = devuelveAlfabetoCodigo(palabrasN)
    HS = entropiaBaseR(prob, len(alf))
    print(HS)
    Ln = longitudMedia(longitudesCodigo(palabrasN), prob)
    print(Ln)
    return (Ln/N >= HS) and (Ln/N < (HS + 1/N))