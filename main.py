from informacion import *
from entropia import *
from fuentes import *
from markov import *

if (__name__ == "__main__"):

    """
    ej 4:
    P = [0.1, 0.3, 0.4, 0.2]
    I = listaInformacion(P)
    print(I)
    print(f"la entropia de las probabilidades es: {Entropia(P,I):.2f} bits")
    """
    """
    ej5:
    """
    """
    alfabeto, prob = devuelveAlfabetoyProbs("CAAACCAABAACBBCABACCAAABCBBACC")
    I = listaInformacion(prob)
    print(alfabeto)
    print(prob)
    print(Entropia(prob, I))
    ej8:
    w = float(input("ingrese un valor para W"))
    print(f"el valor de entropia con w={w} es de: {EntropiaFuenteBinaria(w)}")
    """

    """
    ej10:
    alfa = ['a', 'b', 'c']
    prob = [0.4, 0.3, 0.3]
    N = 3
    extension, p = ExtensionOrdenN(alfa, prob, N)
    print(extension)
    print(p)
    """

    """
    ej11:
    alf = ["x", "y","z"]
    p = [0.5, 0.1, 0.4]
    l=listaInformacion(p)

    ext2, pro2 = ExtensionOrdenN(alf, p, 2)
    informacion2=listaInformacion(pro2)

    print(ext2)
    print(pro2)
    print(f"H(Sn)={Entropia(pro2,informacion2)} n*H(S)={Entropia(p,l)*2}")
    """
    """
    ej14
    """
    Matriz = []
    A = [1/2, 1/3, 0]
    B = [1/2, 1/3, 1]
    C = [0, 1/3, 0]
    Matriz.append(A)
    Matriz.append(B)
    Matriz.append(C)

    print(calcularValorEstacionario(Matriz, 0.1))


"""
1/2 1/3 0
1/2 1/3 1
0   1/3 0

1/3 1/2 1/6
"""