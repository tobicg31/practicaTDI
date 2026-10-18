from entropia import *
from markov import *
from codificacion import *
from fuentes import *


def cumpleTeoremaShannon(prob, palabrasN, N):
    alf = devuelveAlfabetoCodigo(palabrasN)
    
    # Calculamos la entropía total de la extensión y la llevamos por símbolo (dividida por N)
    HS_total = entropiaBaseR(prob, len(alf))
    HS = HS_total / N
    
    # Longitud media total de la extensión y su promedio por símbolo
    Ln_total = longitudMedia(longitudesCodigo(palabrasN), prob)
    Ln_promedio = Ln_total / N
    
    print(f"H(S) por símbolo: {HS}")
    print(f"Ln / N: {Ln_promedio}")
    print(f"Límite superior H(S) + 1/N: {HS + 1/N}")
    
    return (Ln_promedio >= HS) and (Ln_promedio < (HS + 1/N))

class NodoHuffman:
    def __init__(self, simbolo, prob, izq=None, der=None):
        self.simbolo = simbolo
        self.prob = prob
        self.izq = izq
        self.der = der

def generar_diccionario_huffman(nodo, codigo_actual="", codigos=None):
    if codigos is None:
        codigos = {}
        
    if nodo is not None:
        # Si el nodo contiene un símbolo, es una hoja; guardamos su código
        if nodo.simbolo is not None:
            codigos[nodo.simbolo] = codigo_actual
            
        # Recorremos la rama izquierda agregando "0" y la derecha con "1"
        generar_diccionario_huffman(nodo.izq, codigo_actual + "0", codigos)
        generar_diccionario_huffman(nodo.der, codigo_actual + "1", codigos)
        
    return codigos

def algoritmo_huffman(alfabeto, probabilidades):
    # Generar la lista inicial de nodos hoja
    nodos = [NodoHuffman(alfabeto[i], probabilidades[i]) for i in range(len(alfabeto))]

    # Construir el árbol de Huffman uniendo los nodos de menor a mayor probabilidad
    while len(nodos) > 1:
        # Ordenar los nodos por probabilidad
        nodos.sort(key=lambda x: x.prob)

        # Extraer los dos nodos con las probabilidades más bajas
        izq = nodos.pop(0)
        der = nodos.pop(0)

        # Crear un nuevo nodo interno combinando las dos probabilidades
        nodo_padre = NodoHuffman(None, izq.prob + der.prob, izq, der)
        nodos.append(nodo_padre)

    # El único nodo restante es la raíz del árbol
    raiz = nodos[0]
    
    # Retornar el diccionario con los símbolos codificados
    return generar_diccionario_huffman(raiz)

""" def sumaProbs(prob, indice):
    suma=0
    for i in range(indice,len(prob)):
        suma+=prob[i]
    return suma

def corteShannon(codigo):
    i=1
    flag=True
    while flag and (i<len(codigo)):
        flag = codigo[i] == codigo[i-1]
        i+=1
    return flag

def algoritmoShannon(simbolos, prob):
    sumaParcial=0
    codigo= ["" for i in range(len(prob))]
    dicc = dict(zip(simbolos, prob))
    print(dicc)
    print(codigo)
    indice=0
    while(not(corteShannon(codigo))):
        totalProb = sumaProbs(prob, indice) 
        while sumaParcial < totalProb/2:
            sumaParcial += prob[indice]
            indice+=1
        for i in range(indice):
            codigo[i]+= "1"
        for i in range(indice,len(prob)):
            codigo[i] += "0" """

def algoritmoShannon(simbolos, prob):
    # 1. Emparejar símbolos y probabilidades, y ordenarlos de mayor a menor
    elementos = list(zip(simbolos, prob))
    elementos.sort(key=lambda x: x[1], reverse=True)
    
    # Crear el diccionario inicial con cadenas vacías
    dicc_codigos = {simbolo: "" for simbolo, _ in elementos}
    
    # Función recursiva interna para hacer las divisiones
    def dividir(sub_elementos):
        # Condición de corte: si queda 1 solo elemento en este grupo, terminamos
        if len(sub_elementos) <= 1:
            return
        
        # Calcular la probabilidad total de este subgrupo
        total_prob = sum(p for _, p in sub_elementos)
        
        suma_parcial = 0
        diferencia_min = float('inf')
        indice_corte = 0
        
        # 2. Buscar el índice óptimo para cortar (lo más cerca del 50%)
        for i in range(len(sub_elementos)):
            suma_parcial += sub_elementos[i][1]
            # Medimos qué tan lejos estamos de la mitad exacta
            diferencia = abs((total_prob / 2) - suma_parcial)
            
            # Si la diferencia se achica, actualizamos el mejor corte
            if diferencia < diferencia_min:
                diferencia_min = diferencia
                indice_corte = i
            else:
                # Como están ordenados de mayor a menor, si la diferencia 
                # empieza a crecer, significa que ya pasamos el punto óptimo
                break
                
        # 3. Asignar "0" a la primera mitad y "1" a la segunda
        for i in range(indice_corte + 1):
            simbolo = sub_elementos[i][0]
            dicc_codigos[simbolo] += "1"
            
        for i in range(indice_corte + 1, len(sub_elementos)):
            simbolo = sub_elementos[i][0]
            dicc_codigos[simbolo] += "0"
            
        # 4. Llamar a la función recursivamente para cada mitad
        dividir(sub_elementos[:indice_corte + 1])
        dividir(sub_elementos[indice_corte + 1:])
        
    # Arrancar la recursividad con todos los elementos
    dividir(elementos)
    
    return [dicc_codigos[s] for s in simbolos]

def rendimientoYRedunancia(prob, cod):
    entropia = entropiaBaseR(prob, len(devuelveAlfabetoCodigo(cod)))
    long = longitudMedia(longitudesCodigo(cod), prob)
    n = entropia/long
    R = 1-n
    return n, R

def distanciaDeHamming(codigo):
    distanciaMin=9999
    for i in range(len(codigo)):                    #por cada simbolo
        distPalabra=0
        for j in range(len(codigo)):                #comparo con cada simbolo
            if codigo[i] != codigo[j]:              
                for k in range(len(codigo[i])):     #recorro caract a caract
                    if codigo[i][k]!=codigo[j][k]:
                        distPalabra+=1
                if distPalabra < distanciaMin:
                    distanciaMin = distPalabra
    return distanciaMin

def deteccionCorrecion(hamming):
    det = hamming -1
    corr = floor((hamming -1)/2)
    return det, corr

