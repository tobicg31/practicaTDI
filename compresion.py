from codFuente import *
from paridad import *

def huffmanYshannonString(probs):
    huff = algoritmo_huffman(range(len(probs)), probs)
    shan = algoritmoShannon(range(len(probs)), probs)
    huffString = "".join(huff.values())
    shanString = "".join(shan)
    return huffString, shanString

def mensajeCodificado(codigo):
    codificado = ""
    codificado += "".join(codigo)
    return arregloBytes(codificado)

def binario_a_matriz(binario, columnas):
    # Nos aseguramos de que el binario sea un string para poder iterarlo
    cadena_binaria = str(binario)
    matriz = []
    
    # Recorremos la cadena dando saltos del tamaño de las columnas
    for i in range(0, len(cadena_binaria), columnas):
        # Extraemos el fragmento correspondiente a la fila actual
        fragmento = cadena_binaria[i : i + columnas]
        
        # Convertimos cada '0' o '1' en un número entero y lo guardamos como fila
        fila = [int(bit) for bit in fragmento]
        matriz.append(fila)
        
    return matriz

def mensajeDescodificado(bytes):
    

    return recuperoMensaje(matrizParidad)