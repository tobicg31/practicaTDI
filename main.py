from informacion import *
from entropia import *
from fuentes import *
from markov import *
from codificacion import *

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
    """
    Matriz = [
        [1/2, 1/2, 0], 
        [1/3, 1/3, 1/3],
        [0, 1, 0]
        ]
    print(calcularValorEstacionario(Matriz, 0.00000001))
    ej15:
    mensaje = ";;,;,;:,,,.;,,.,,,::,;;;,:;.,,;:,,,:..;,;;.,;,,.:;"
    alf, prob = devuelveAlfabetoyProbs(mensaje)
    print(alf, prob)
    matriz = calcularMatrizTransicion(mensaje,alf)
    print(matriz)
    print(devuelvecadenadimensionN(8,alf,matriz))
    print(esFuenteMemoriaNula(matriz, 0.001))
    vec = calcularValorEstacionario(matriz, 0.001)
    print(EntropiaMarkov(vec,matriz))
    """
    """
    guia 3, ej6
    fuente = ["A","B","C","D"]
    codigo = ["0","01","10"]
    print(esNoSingular(codigo))
    s = esUnivocamente(codigo)
    print(s)
    print(esInstantaneo(codigo))
    """
    """
    ej10 y 12 
    codigo1= [".,", ";",",,",":","...",",:;"]
    print(f"es noS:{esNoSingular(codigo1)} es Uni:{esUnivocamente(codigo1)}")
    print(f"es instan: {esInstantaneo(codigo1)}")
    
    alf = devuelveAlfabetoCodigo(codigo1)
    print(f"el alfabeto es: {alf}")

    p = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]
    inform = informacionTecho(listaInformacion(p))
    print(f"sus informaciones: {inform}")

    longitudes = longitudesCodigo(codigo1)
    print(f"sus longitudes: {longitudes}")

    print(f"la sumatoria de kraft da: {sumatoriaKraft(codigo1, longitudes, len(alf))}")
    print(f"la entropia es: {entropiaBaseR(p, len(alf))}")
    print(f"la longitud media es: {longitudMedia(longitudes, p)}")
    """

    """
    ej13:
    p = [0.5, 0.25,0.125, 0.125]
    print(informacionTecho(infoBaseR(p,3)))
    """

    codigo= ["1","21","31","32"]
    p = [0.5, 0.25,0.125, 0.125]


    print(esUnivocamente(codigo))
    print(esInstantaneo(codigo))
    print(informacionTecho(infoBaseR(p,3)))
    print(longitudesCodigo(codigo))
    print(esCompacto(codigo,p,3))