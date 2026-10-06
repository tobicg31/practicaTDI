from math import *
"""
Dados la distribución de probabilidades de una fuente y el siguiente código:

Comprobar si cumple la inecuación de Kraft-McMillan
Calcular la entropía de la fuente y la longitud media del código
Determinar si se trata de un código compacto
Proponer otro código compacto con el mismo alfabeto para la fuente
"""
def informacionTecho(info):
    return [ ceil(info[i]) for i in range(len(info))]

def longitudesCodigo(codigo):
    return [ len(codigo[i]) for i in range(len(codigo))]

def devuelveAlfabetoCodigo(codigo): 
    caracteres = ""

    for i in range(len(codigo)):
        for j in range(len(codigo[i])):
            if not(caracteres.__contains__(codigo[i][j])):
                caracteres += codigo[i][j]

    return caracteres


def entropiaBaseR(p,r):
    s=0
    for i in range(len(p)):
        s += p[i]*log(1/p[i],r)
    return s

def sumatoriaKraft(codigo, long,r):
    acum = 0
    for i in range(len(codigo)):
        acum += pow(r,-1*long[i])
    return acum

def longitudMedia(long, p):
    acum=0
    for i in range(len(long)):
        acum += p[i]*long[i]
    return acum

def esCompacto(codigo, p,r):
    f = True
    i=0
    while( f and i < len(codigo)):
        f = len(codigo[i]) <= ceil(log(1/p[i],r))
        i += 1
    return f
def esInstantaneo(codigo):
    f=False
    i=0
    while (i<len(codigo) and not(f)):
        j=1
        while (j<len(codigo) and not(f)):
            if (len(codigo[i]) > len((codigo[j])) ):
                f = codigo[i].startswith(codigo[j])
            j+=1
        i+=1

    return not(f)

if (__name__ == "__main__"):
    prob = [1/3, 1/9, 1/9, 1/3, 1/9]
    codigo = ["A", "AB", "BC", "B", "CA"]
    longitudes = longitudesCodigo(codigo)
    r = len(devuelveAlfabetoCodigo(codigo))

    print("la inecuacion de kraft-mcmillan: ", sumatoriaKraft(codigo, longitudes, r))
    print("la entropia Hr(S): ", entropiaBaseR(prob, r))
    print("longitud media: ", longitudMedia(longitudes, prob))
    if (esInstantaneo(codigo)):
        print("es compacto?: ", esCompacto(codigo, prob, r))

    codigoNuevo = ["A", "BB", "BA", "C", "BC"]
    if (esInstantaneo(codigoNuevo)):
        print("es compacto el codigo nuevo?: ", esCompacto(codigoNuevo, prob, r))