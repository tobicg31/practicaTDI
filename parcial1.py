from codificacion import *
from entropia import *
from fuentes import *
from informacion import *
from markov import *

if (__name__ == "__main__"):
    """
    prob = [0.15, 0.25, 0.05, 0.45, 0.1]
    codigo = ["/+", "*", "+-", "-", "*/"]
    alfabeto = devuelveAlfabetoCodigo(codigo)
    print("Hr(S): ", entropiaBaseR(prob, len (alfabeto)))
    r = len(alfabeto)
    print("longitud media: ", longitudMedia(longitudesCodigo(codigo), prob))
    print("inecuacion: ", sumatoriaKraft(codigo, longitudesCodigo(codigo), r))

    """
    """"

    print("es no singular?: ",esNoSingular(codigo))
    print("es instantaneo?: ", esInstantaneo(codigo))
    if esInstantaneo(codigo):
        print("es compacto?: ", esCompacto(codigo, prob, r))
    """
    prob = [0.15, 0.25, 0.05, 0.45, 0.1]
    codigo = ["(]", "]", "[)", ")", "(["]
    alfabeto = devuelveAlfabetoCodigo(codigo)
    print("Hr(S): ", entropiaBaseR(prob, len (alfabeto)))
    r = len(alfabeto)
    print("longitud media: ", longitudMedia(longitudesCodigo(codigo), prob))
    print("inecuacion: ", sumatoriaKraft(codigo, longitudesCodigo(codigo), r))

    print("es no singular?: ",esNoSingular(codigo))
    print("es instantaneo?: ", esInstantaneo(codigo))

    print("es univoco?: ",esUnivocamente(codigo))

    print("longitudes: ", longitudesCodigo(codigo))
    print("infos: ", [round(x,1) for x in informacionTecho(listaInformacion(prob))])

    if esInstantaneo(codigo):
        print("es compacto?: ", esCompacto(codigo, prob, r))