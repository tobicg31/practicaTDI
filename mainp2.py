from codFuente import *

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
    """
    w = 0.7
    alf = ["1","0"]
    extN, probN = ExtensionOrdenN(alf, [w, 1-w], 2)
    codigos = algoritmo_huffman(extN, probN)
    for simbolo, codigo in codigos.items():
        print(f"Símbolo: {simbolo} | Código: {codigo}")