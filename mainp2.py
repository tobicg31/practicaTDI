from codFuente import *
from paridad import *

if (__name__ == "__main__"):
    """
    ej2:
    prob = [0.3, 0.1, 0.4, 0.2]
    codigo = ["BA", "CAB", "A", "CBA"]

    print(cumpleTeoremaShannon(prob, codigo, 2))
    """

    """
    ej3:
    prob = [0.5, 0.2, 0.3]
    cod = ["11", "010", "00"]
    C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]

    print(cumpleTeoremaShannon(prob, cod, 2))
    """
    """
    ej4:
    w = 0.8
    alf = ["1","0"]
    extN, probN = ExtensionOrdenN(alf, [w, 1-w], 3)
    print(extN)
    print(probN)
    print("H(S): ", entropiaBaseR(probN, 2), "H(S)+1/N: ",entropiaBaseR(probN, 2)+1/3)
    codigos = algoritmo_huffman(extN, probN)
    print(codigos)
    for simbolo, codigo in codigos.items():
        print(f"Símbolo: {simbolo} | Código: {codigo}")
    palabras_codigo = list(codigos.values())
    print(cumpleTeoremaShannon(probN, palabras_codigo, 3))
    """
    
    """
    ej5:
    w = 0.7
    alf = ["1","0"]
    extN, probN = ExtensionOrdenN(alf, [w, 1-w], 2)
    codigos = algoritmo_huffman(extN, probN)
    for simbolo, codigo in codigos.items():
        print(f"Símbolo: {simbolo} | Código: {codigo}")

    codigo = algoritmoShannon(extN, probN)
    print(codigo)
    print(cumpleTeoremaShannon(probN, codigo, 2))
    n, R = rendimientoYRedunancia(probN, codigo)
    print(n, R)
    """

    """
    ej8:
    prob = [0.2, 0.15, 0.1, 0.3, 0.25]
    codigo1= ["01", "111", "110", "101", "100"]
    n, R = rendimientoYRedunancia(prob, codigo1)
    print(n, R)
    """

    """
    ej9:
    cod = ["0110000","0000011","0101101","0100110"]
    dist = distanciaDeHamming(cod)
    print(dist)
    print(deteccionCorrecion(dist))
    """

    """
    ej12:
    print(ascii("a"))
    print(verificoAscii(ascii("a"), 195))
    """

    """
    ej13:
    matriz = [[0,0,1,0,0,0,0,1], [1,0,0,0,0,1,1,1], [1,0,0,0,0,0,1,0], [1,0,1,0,0,1,1,0], [1,0,0,0,0,0,1,0]]
    matriz2 = [
        [0,0,1,0,1,1,0,1],
        [1,0,0,1,1,0,0,1],
        [1,0,0,0,1,0,1,0],
        [1,0,0,1,1,1,0,0],
        [1,0,0,0,0,0,1,0],
    ]
    #print(len(matriz))
    #print(len(matriz[1]))
    print("")
    #print(detectarErrorParidad(matriz))
    print(recuperoMensaje(matriz))
    print(recuperoMensaje(matriz2))
    """

    """
    ej14:
    """
    print(bin(arregloBytes("CASA")))