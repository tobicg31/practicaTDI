from markov import *
from entropia import *

def MatrizPba(alfE, alfS,entrada, salida):
    """
    le paso alfabetos y los msg de entrada y salida y devuelve
    la matriz del canal P(bj/ai)
    """
    aparicionesE = [cantApariciones(i, entrada) for i in alfE]
    aparicionesS = [cantApariciones(i, salida) for i in alfS]
    matriz = []
    for i in range(len(aparicionesE)):
        matriz.append([])
        for j in range(len(aparicionesS)):
            matriz[i].append(0) 

    for c in range(len(alfE)):
        for i in range(len(entrada)):
            if entrada[i]==alfE[c]:
                matriz[c][int(salida[i])] +=1
        for i in range(len(alfS)):
            matriz[c][i] /= aparicionesE[c]

    return matriz

def probSalida(matriz, probPriori):
    """
    le paso la matriz del canal y las probabilidades a priori P(ai)
    y devuelve las probabilidades de salida P(bj)
    """
    pSalida = []
    for i in range(len(matriz[1])):
        pSalida.append(0)

    for k in range(len(matriz[1])):
        for i in range(len(probPriori)):
            pSalida[k] += probPriori[i]*matriz[i][k]
    
    return pSalida

def probPosteriori(matriz, priori, salida):
    """
    le paso la matriz de canal, P(ai), P(bj)
    y devuelve las probabilidades a posteriori P(ai/bj)
    """
    poste = []
    for i in range(len(matriz)):
        poste.append([])
        for j in range(len(matriz[1])):
            poste[i].append((matriz[i][j]*priori[i])/salida[j]) 
    return (poste)

def probSimultaneos(matriz, salida):
    """
    le paso la matriz del canal y P(bj)
    y devuelve las probabilidades simultaneas P(ai, bj)
    """
    simul = []
    for i in range(len(matriz)):
        simul.append([])
        for j in range(len(matriz[1])):
            simul[i].append((matriz[i][j])*salida[j]) 

    return (simul)

def entropiaPriori(priori):
    """
    le paso las prob a priori P(ai)
    y devuelve su entropia H(A)
    """
    return Entropia(priori, listaInformacion(priori))

def entropiaPosteriori(priori, matriz):
    """
    le paso las prob a priori P(ai) y la matriz del canal
    y devuelve las entropias a posteriori H(A/bj)
    """
    Hpost = [] 
    salida = probSalida(matriz, priori)
    posteriori = probPosteriori(matriz, priori, salida)
    for i in range(len(salida)):
        col = []
        for k in range(len(priori)):
            col.append(posteriori[k][i])
        Hpost.append(entropiaPriori(col))
    return Hpost

def equivocacion(salida, Hpost):
    """
    le paso las prob de salida P(bj) y la entropia a post H(A/bj)
    y devuelve la equivocacion/ruido H(A/B)
    """
    equi = 0
    for i in range(len(salida)):
        equi+= salida[i]*Hpost[i]
    return equi

def perdida(equi, Hpriori, Hsalida):
    """
    le paso la equivocacion H(A/B), las entropias a priori H(A) y de salida H(B)
    y devuelve la perdida H(B/A)
    """
    return equi + Hsalida - Hpriori

def entropiaAfin(Ha, Hba):
    """
    le paso la entropia a priori H(A) y la perdida
    y devuelve la entropia conjunta/afin H(A,B)
    """
    return Ha+Hba

def informacionMutua(Hb, Hba):
    """
    le paso la entropia de salida H(B) y la perdida
    y devuelve la inform mututa I(A, B)
    
    """
    return Hb-Hba

def esSinRuido(matriz):
    """
    le paso una matriz y devuelve si es sin ruido o no
    revisa si hay mas de un elemento != 0 por columna
    """
    cont = []
    for k in range(len(matriz[1])):
        cont.append(0)

    for j in range(len(matriz[1])):
        for i in range(len(matriz)):
            if matriz[i][j] > 0:
                cont[j] += 1

    k =0
    bool = False
    while (k <len(cont)) and not(bool) :
        bool = cont[k]>1
        k+=1
    return not(bool)

def esDeterminante(matriz):
    """
    le paso una matriz y devuelve si es determinante o no
    revisa si hay mas de un elemento != 0 por fila
    """
    cont = []
    for k in range(len(matriz)):
        cont.append(0)

    for i in range(len(matriz)):
        for j in range(len(matriz[1])):
            if matriz[i][j] > 0:
                cont[i] += 1

    k =0
    bool = False
    while (k <len(cont)) and not(bool) :
        bool = cont[k]>1
        k+=1
    return not(bool)

def matrizCompuesto(a, b):
    """
    le paso dos matrices y las multiplica basically
    """
    prod = []
    for i in range(len(a)):
        prod.append([])
        for j in range(len(b[1])):
            prod[i].append(0.0) 

    for i in range(len(a)):
        for j in range(len(b[1])):
            for k in range(len(b)):
                prod[i][j] += a[i][k] * b[k][j]
    return prod

def verificoCombinacion(matriz, i, j):
    constante = None
    
    for fila in matriz:
        val_i = fila[i]
        val_j = fila[j]
        
        # Validación de divisor nulo
        if val_j == 0:
            if val_i != 0:
                return False  # No existe k tal que k * 0 = val_i (val_i != 0)
            continue  # 0 y 0 son compatibles con cualquier constante
        
        ratio = val_i / val_j
        
        # Asignación o comparación de la razón de proporcionalidad
        if constante is None:
            constante = ratio
        elif not math.isclose(ratio, constante, rel_tol=1e-7):
            return False
            
    return True
    
def generar_matriz_T(matriz):
    num_columnas = len(matriz[0])
    grupos = []             # Guarda los índices de la columna representante de cada grupo
    asignaciones = [-1] * num_columnas
    
    # Clasificar cada columna 'j' comparándola con los representantes existentes 'col_rep'
    for j in range(num_columnas):
        encontrado = False
        for idx_grupo, col_rep in enumerate(grupos):
            if verificoCombinacion(matriz, j, col_rep):
                asignaciones[j] = idx_grupo
                encontrado = True
                break
        if not encontrado:
            grupos.append(j)
            asignaciones[j] = len(grupos) - 1

    # Construir la matriz T (dimensión: num_columnas x len(grupos))
    T = [[0] * len(grupos) for _ in range(num_columnas)]
    for j in range(num_columnas):
        grupo_idx = asignaciones[j]
        T[j][grupo_idx] = 1
        
    return T

def reducirMatriz(matriz):
    T = generar_matriz_T(matriz)
    producto = matrizCompuesto(matriz, T)
    return producto

def capacidadDet(matriz):
    """
    capacidad si es det, log(nro salidas)
    """
    return log(len(matriz[1]))

def capacidadSinRuido(matriz):
    """
    capacidad si es sin ruido, log(nro entradas)
    """
    return log(len(matriz))

def capacidadBinario(matriz, paso):
    capacidad = 0
    pActual = 0

    cantPasos = round(1/paso)

    for indicePaso in range(1, cantPasos):
        pSimbolo = indicePaso*paso
        priori = [pSimbolo, 1-pSimbolo]

        salida = probSalida(matriz, priori)
        Ha = entropiaPriori(priori) #ENTROPIA FUENTE
        Hb = entropiaPriori(salida) #ENTROPIA SALIDA

        Hab = entropiaPosteriori(priori, matriz) #ENTROPIA POSTERIORI
        HaB = equivocacion(salida, Hab) #EQUIVOCACION 
        Hba = perdida(HaB, Ha, Hb) #PERDIDA

        Iab = informacionMutua(Hb, Hba) #INFORMACION MUTUA
        if Iab > capacidad:
            capacidad = Iab
            pActual = pSimbolo
    return capacidad, pActual

def probError(matriz, priori):
    Pe = 0

    for i in range(len(matriz[0])):
        min = 9
        jMin = 0
        for j in range(len(matriz)):
            if matriz[j][i] < min:
                min=matriz[j][i]
                jMin = j
        Pe += min*priori[jMin]
    return Pe