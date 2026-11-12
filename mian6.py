from libreria import *
if (__name__ == "__main__"):

    """
    ej1:
    alfEntrada = ["a","b","c"]
    alfSalida = ["0", "1"]
    mensaje = "abcacaabbcacaabcacaaabcaca"
    salida = "01010110011001000100010011"
    print(len(mensaje), len(salida))
    matri = MatrizPba(alfEntrada, alfSalida, mensaje, salida)
    print(matri)
    print(devuelveProbabilidad(mensaje, alfEntrada))
    """
    
    """
    ej6 y 7:
    matriz = [[0.4, 0.4, 0.2], [0.3, 0.2, 0.5], [0.3, 0.4, 0.3]]
    probPriori = [0.3, 0.3, 0.4]
    probsalida = probSalida(matriz, probPriori)
    posteriori = probPosteriori(matriz, probPriori, probsalida)   
    probSimultaneos(posteriori, probsalida)
    """

    """
    ej8:
    mensaje = "abcacaabbcacaabcacaaabcaca"
    alfEntrada = ["a","b","c"]
    alfSalida = ["0", "1"]
    salida = "01010110011001000100010011"
    priori= devuelveProbabilidad(mensaje, alfEntrada)
    print(priori)

    matriz = MatrizPba(alfEntrada, alfSalida, mensaje, salida)
    print(matriz)

    salida = probSalida(matriz, priori)
    print(salida)
    """

    """
    ej10y11:
    priori =  [2/5, 3/5] 
    print(entropiaPriori(priori))

    matriz = [[3/5, 2/5],[1/3, 2/3]]
    print(entropiaPosteriori(priori,matriz))
    """

    """
    ej13:
    priori = [ 0.14, 0.52, 0.34 ]
    matri = [[0.50, 0.30, 0.20 ], [0.00, 0.40, 0.60], [0.20,0.80, 0.00]]
    print(entropiaPriori(priori))
    salida = probSalida(matri, priori)
    posteriori = probPosteriori(matri, priori, salida)
    print(salida)
    print(posteriori)
    print(entropiaPosteriori(priori, matri))
    """

    """
    ej14:
    priori = [ 0.70, 0.30]
    matriz = [[0.7, 0.3], [0.4, 0.6 ]]
    Hpriori = entropiaPriori(priori)
    print("entropia priori:", Hpriori)

    salida =probSalida(matriz, priori)
    print("prob salidas:",salida)

    Hsalida =entropiaPriori(probSalida(matriz, priori))
    print("entropia salida", Hsalida) #entropia de salida

    Hpost = entropiaPosteriori(priori, matriz)
    print("entropia posteriori",Hpost)

    equi = equivocacion(salida, Hpost)
    print("equivocacion:",equi)

    perdi = perdida(equi, Hpriori, Hsalida)
    print("perdida:", perdi)

    infMutua = informacionMutua(Hsalida, perdi)
    print(infMutua)

    afin = entropiaAfin(Hpriori, perdi)
    print(afin)
    """

    """
    ej17:
    matriz1 = [[0.0, 1.0, 0.0], [0.0, 0.0, 1.0 ], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0 ]]
    matriz2= [[1.0, 0.0, 0.0, 0.0],[0.0, 0.2, 0.0, 0.8 ],[0.0, 0.0, 1.0, 0.0 ]]
    matriz3 = [[0.0, 0.0, 1.0, 0.0 ],[1.0, 0.0, 0.0, 0.0],[0.0, 1.0, 0.0, 0.0 ],[0.0, 0.0, 0.0, 1.0]]
    print("Son sin ruido?:")
    print(esSinRuido(matriz1))
    print(esSinRuido(matriz2))
    print(esSinRuido(matriz3))
    print()

    print("Son determinante?:")
    print(esDeterminante(matriz1))
    print(esDeterminante(matriz2))
    print(esDeterminante(matriz3))
    print()

    priori1 = [1/4,1/4,1/4,1/4]
    Hpriori1 = entropiaPriori(priori1)
    salida1 = probSalida(matriz1, priori1)
    Hsalida1 = entropiaPriori(salida1)
    Hpost1 = entropiaPosteriori(priori1, matriz1)
    equi1 = equivocacion(salida1, Hpost1)
    print("ruido: ", equi1)
    perdi1 = perdida(equi1, Hpriori1, Hsalida1)
    print("perdida", perdi1)
    infmutua1 = informacionMutua(Hsalida1, perdi1)
    print("informacion mutua: ", infmutua1)
    """

    """
    ej19
    a = [[0.7, 0.0, 0.3, 0.0 ], [0.2, 0.6, 0.0, 0.2 ]]
    b = [[0.9, 0.0, 0.1 ], [0.0, 1.0, 0.0], [0.1, 0.1, 0.8], [0.0, 0.5, 0.5 ]]
    print(matrizCompuesto(a, b))
    """

    """
    ej21y22y23:
    matriz = [[0.0, 0.5, 0.0, 0.5],
              [0.8, 0.0, 0.2, 0.0],
              [0.0, 0.5, 0.0, 0.5],
              [0.8, 0.0, 0.2, 0.0]]

    matriz2 = [
        [0.4, 0.6, 0.0, 0.0 ],
        [0.0, 0.0, 0.5, 0.5],
        [0.0, 0.0, 0.7, 0.3]
    ]
    print(reducirMatriz(matriz))
    print(reducirMatriz(matriz2))
    """

    """
    ej26y27:
    EH no entiendo
    matriz = [[0.25, 0.75 ], [0.90, 0.10 ]]
    capacidad, prob = capacidadBinario(matriz, 0.00001)
    print(capacidad, prob)
    """


    """
    ej28y30 listo por dios:
    """
    matriz = [0.6, 0.4], [0.2, 0.8]

    print(probError(matriz, [0.5, 0.5]))