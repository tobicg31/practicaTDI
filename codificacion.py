from math import *

def esNoSingular(codigo):
    f = True
    i=0
    j=0
    while (f and j < len(codigo)):
        while (f and i < len(codigo)):
            if (j != i):
                f = codigo[j] != codigo[i]
            i+=1
        j+=1
    return f

def esUnivocamente(codigo):
    """
    esto lo hizo Claude y creo que esta mal
    ta bien lpm
    Determina si un codigo es univocamente decodificable aplicando
    el algoritmo de Sardinas-Patterson.
 
    Parametros:
        codigo (list): lista de palabras codigo (strings), por ejemplo
                        ["0", "01", "11"].
 
    Retorna:
        bool: True si el codigo es univocamente decodificable,
              False en caso contrario.
    """
    if len(codigo) != len(set(codigo)):
        raise ValueError("El codigo contiene palabras repetidas.")
 
    C0 = set(codigo)
 
    def sufijo(mas_larga, mas_corta):
        """
        Si 'mas_corta' es prefijo de 'mas_larga' (y son distintas),
        devuelve el sufijo restante. En caso contrario, devuelve None.
        """
        if mas_larga != mas_corta and mas_larga.startswith(mas_corta):
            return mas_larga[len(mas_corta):]
        return None
 
    def calcular_siguiente_conjunto(conjunto_anterior, codigo_original):
        """
        Genera Cn a partir de C0 y C(n-1), combinando ambos conjuntos
        en las dos direcciones posibles (segun la definicion del
        algoritmo de Sardinas-Patterson).
        """
        nuevo_conjunto = set()
 
        for palabra_codigo in codigo_original:
            for residuo in conjunto_anterior:
                s = sufijo(palabra_codigo, residuo)
                if s is not None:
                    nuevo_conjunto.add(s)
 
                s = sufijo(residuo, palabra_codigo)
                if s is not None:
                    nuevo_conjunto.add(s)
 
        return nuevo_conjunto
 
    # C1 se construye comparando C0 consigo mismo
    conjunto_actual = calcular_siguiente_conjunto(C0, C0)
    conjuntos_vistos = []
 
    while True:
        # Criterio de Sardinas-Patterson: si Cn (n>=1) intersecta con C0,
        # el codigo NO es univocamente decodificable.
        if conjunto_actual & C0:
            return False
 
        # Si Cn queda vacio, no se pueden generar mas sufijos: es UDC.
        if not conjunto_actual:
            return True
 
        # Si el conjunto ya aparecio antes, entramos en un ciclo sin
        # haber intersectado nunca con C0: el codigo es UDC.
        if conjunto_actual in conjuntos_vistos:
            return True
 
        conjuntos_vistos.append(conjunto_actual)
        conjunto_actual = calcular_siguiente_conjunto(conjunto_actual, C0)


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

"""
ej9a:
"""
def devuelveAlfabetoCodigo(codigo): 
    caracteres = ""

    for i in range(len(codigo)):
        for j in range(len(codigo[i])):
            if not(caracteres.__contains__(codigo[i][j])):
                caracteres += codigo[i][j]

    return caracteres

"""
ej9b:
"""
def informacionTecho(info):
    return [ ceil(info[i]) for i in range(len(info))]

def longitudesCodigo(codigo):
    return [ len(codigo[i]) for i in range(len(codigo))]

"""
ej9c:
"""
def sumatoriaKraft(codigo, long,r):
    acum = 0
    for i in range(len(codigo)):
        acum += pow(r,-1*long[i])
    return acum


"""
ej10a:
"""
def entropiaBaseR(p,r):
    s=0
    for i in range(len(p)):
        s += p[i]*log(1/p[i],r)
    return s

"""
ej10b:
"""
def longitudMedia(long, p):
    acum=0
    for i in range(len(long)):
        acum += p[i]*long[i]
    return acum

def infoBaseR(p, r):
    return [log(1/p[i],r) for i in range(len(p))]


"""
ej14:
"""
def esCompacto(codigo, p,r):
    f = True
    i=0
    while( f and i < len(codigo)):
        f = len(codigo[i]) <= ceil(log(1/p[i],r))
        i += 1
    return f

