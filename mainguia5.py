from codFuente import *
from codificacion import *
from compresion import * 

if (__name__ == "__main__"):

    """
    ej1:
    simbolos = ["1", "2", "3", "4"]
    probA = [0.2, 0.2, 0.3, 0.3]
    huffman = algoritmo_huffman(simbolos, probA)
    shannon = algoritmoShannon(simbolos, probA)

    print(huffman)
    print(shannon)
    """

    """
    ej2:
    mensaje = "ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB"
    alf, prob = devuelveAlfabetoyProbs(mensaje)
    huffman = algoritmo_huffman(alf, prob)
    print(huffman)

    shannon = algoritmoShannon(alf, prob)
    print(shannon)
    """

    """
    ej3:
    prob = [0.1, 0.4, 0.2, 0.3]
    huffman, shannon = huffmanYshannonString(prob)
    print(huffman)
    print(shannon)
    prob = [0.385, 0.154, 0.128, 0.154, 0.179]
    entropia = entropiaBaseR(prob, 2)
    print(entropia)
    huffman = algoritmo_huffman(range(len(prob)),prob)
    shannon = algoritmoShannon(range(len(prob)),prob)
    print(huffman, shannon)

    print("huffman: \nlongitudes: ", longitudMedia(longitudesCodigo(huffman), prob))
    n, R = rendimientoYRedunancia(prob, huffman)
    print("rendimiento: ", n, " redundancia: ", R)

    print("shannon: \nlongitudes: ", longitudMedia(longitudesCodigo(shannon), prob))
    n, R = rendimientoYRedunancia(prob, shannon)
    print("rendimiento: ", n, " redundancia: ", R)
    """

    """
    ej5:
    mensaje = "58784784525368669895745123656253698989656452121702300223659"
    alf, prob = devuelveAlfabetoyProbs(mensaje)
    entropiaFuente = entropiaBaseR(prob, 2)
    print(entropiaFuente)
    huffman = algoritmo_huffman(range(len(prob)),prob)
    shannon = algoritmoShannon(range(len(prob)),prob)
    print(huffman, shannon)

    print("huffman: \nlongitudes: ", longitudMedia(longitudesCodigo(huffman), prob))
    n, R = rendimientoYRedunancia(prob, huffman)
    print("rendimiento: ", n, " redundancia: ", R)

    print("shannon: \nlongitudes: ", longitudMedia(longitudesCodigo(shannon), prob))
    n, R = rendimientoYRedunancia(prob, shannon)
    print("rendimiento: ", n, " redundancia: ", R)
    """

    """
    ej7:
    """
    mensaje= "CBCCBBBCAABBCBABCB"
    alf, prob = devuelveAlfabetoyProbs(mensaje)
    huffman, shannon = huffmanYshannonString(prob)
    print(mensajeCodificado(huffman))