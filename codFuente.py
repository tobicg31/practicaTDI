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
