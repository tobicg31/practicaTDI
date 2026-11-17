from codFuente import *
from paridad import *

def huffmanYshannonString(probs):
    huff = algoritmo_huffman(range(len(probs)), probs)
    shan = algoritmoShannon(range(len(probs)), probs)
    huffString = "".join(huff.values())
    shanString = "".join(shan)
    return huffString, shanString

#def mensajeCodificado(codigo):
    codificado = ""
    codificado += "".join(codigo)
    return arregloBytes(codificado)

def codificar_mensaje_a_bytes(mensaje, alfabeto, codigos):
    # 1. Armamos un diccionario para buscar rápido: 'A' -> '01', 'B' -> '10', etc.
    dicc_codigos = {alfabeto[i]: codigos[i] for i in range(len(alfabeto))}
    
    # 2. Traducimos el mensaje original a una tira de unos y ceros
    bits_str = "".join([dicc_codigos[letra] for letra in mensaje])
    
    # 3. Rellenamos con ceros al final para que la longitud total sea múltiplo de 8
    bits_faltantes = (8 - len(bits_str) % 8) % 8
    bits_str += '0' * bits_faltantes
    
    # 4. Convertimos de a 8 bits a enteros y lo guardamos en un bytearray
    secuencia_bytes = bytearray()
    for i in range(0, len(bits_str), 8):
        byte_cadena = bits_str[i:i+8]
        secuencia_bytes.append(int(byte_cadena, 2)) # int(..., 2) castea de binario a entero
        
    return secuencia_bytes

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

def decodificar_desde_bytes(alfabeto, codificacion, secuencia_bytes):
    # 1. Armamos un diccionario inverso para buscar rápidamente qué letra corresponde a cada código binario
    dicc_inverso = {codificacion[i]: alfabeto[i] for i in range(len(alfabeto))}
    
    # 2. Reconstruimos la cadena larga de ceros y unos a partir de la secuencia de bytes
    # bin(byte) devuelve algo como '0b101', le sacamos el '0b' con [2:] y rellenamos con ceros a la izquierda hasta 8 bits (zfill)
    cadena_bits = "".join([bin(byte)[2:].zfill(8) for byte in secuencia_bytes])
    
    # 3. Recorremos la cadena bit a bit para reconstruir el mensaje original
    mensaje_original = ""
    buffer_bits = ""
    
    for bit in cadena_bits:
        buffer_bits += bit
        
        # Si la secuencia que venimos acumulando forma un código válido, guardamos la letra
        if buffer_bits in dicc_inverso:
            mensaje_original += dicc_inverso[buffer_bits]
            buffer_bits = "" # Vaciamos el buffer para buscar la siguiente letra
            
    return mensaje_original

def RLC(mensaje):
    codificado = ""
    act = mensaje[0]
    cont=1
    contadores = []
    for i in range(1,len(mensaje)):
        if mensaje[i] == act:
            cont+=1
        else:
            codificado += act
            contadores.append(cont)
            act = mensaje[i]
            cont=1
    codificado += act
    contadores.append(cont)

    rlc = ""
    for i in range(len(codificado)):
        rlc += codificado[i]
        rlc += str(contadores[i])
    return rlc

def bytesRLC(mensaje):
    rlc = RLC(mensaje)
    secuencia_bytes = bytearray()
    
    i = 0
    while i < len(rlc):
        letra = rlc[i]
        i += 1
        
        numero_str = ""
        while i < len(rlc) and rlc[i].isdigit():
            numero_str += rlc[i]
            i += 1
            
        secuencia_bytes.append(ord(letra))
        secuencia_bytes.append(int(numero_str))
        
    return secuencia_bytes

def tasaCompresion(mensaje, bytes):
    largoMensaje= len(mensaje)
    largoBytes = len(bytes)
    print("\n",largoMensaje, ":", largoBytes)
    return largoMensaje / largoBytes