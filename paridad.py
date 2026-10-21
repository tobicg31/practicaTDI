def calculoParidad(codigo):
    cant1 = 0
    while (codigo != 0):
        cant1 += codigo & 0x1
        codigo = codigo >> 1
    return cant1 % 2

def calculoParidadLista(codigo):
    cant = 0
    for i in range(len(codigo)):
        if codigo[i]==1:
            cant +=1
    return cant%2
    
def ascii(char):
    codigo = ord(char)
    paridad = calculoParidad(codigo)
    codificado = (codigo << 1) | paridad 
    return codificado

def verificoAscii(original, ache):
    if original == ache:
        return "todo pelota"
    if (original & 0x1) != (ache & 0x1):
        return "ta mal la paridad"
    if (original >> 1) != (ache >> 1):
        return "ta mal el cod en ascii"

def asciint(codigo):
    car=0
    for i in range(len(codigo)):
        car = car<<1 | codigo[i]
    return chr(car>>1)

def detectarErrorParidad(matriz):
    columnas = [0 for i in range(len(matriz[0])-1)]
    filas = [0 for i in range(len(matriz))]
    #verifico filas
    for i in range(1,len(matriz)):
        fila = [matriz[i][k] for k in range(len(matriz[0])-1)]
        if calculoParidadLista(fila) == matriz[i][len(matriz[0])-1]:
            filas[i] += 1

    #verifico columnas
    for i in range(len(matriz[0])-1):
        columna = [matriz[k][i] for k in range(len(matriz)-1)]
        if calculoParidadLista(columna) == matriz[len(matriz)-1][i]:
            columnas[i] += 1

    #reviso par cruzada
    priFila = [matriz[0][k] for k in range(len(matriz[0])-1)]
    ultCol = [matriz[k][len(matriz[0])-1] for k in range(len(matriz)-1)]
    cumpleCruzada = calculoParidadLista(priFila) == calculoParidadLista(ultCol)
    
    return filas, columnas, cumpleCruzada

def recuperoMensaje(matriz):
    mensaje=""
    filas, columnas, cruz = detectarErrorParidad(matriz)
    for i in range(1,len(filas)):
        if (filas[i] != 1):
            mensaje += "¨"
        else:
            mensaje += asciint(matriz[i])
    return mensaje

def arregloBytes(cadena):
    locura = 0
    for i in range(len(cadena)):
        locura = locura<<8 | ascii(cadena[i])
    
    ultimaFila=0
    for bit_pos in range(7, -1, -1):
        col = []
        for k in range(len(cadena)):
            # Tomamos el valor de la letra en esa fila
            caracter = ascii(cadena[k])
            
            # Desplazamos el caracter para que el bit que queremos quede a la derecha
            # y usamos & 1 para borrar todo lo demás y quedarnos solo con ese '0' o '1'
            bit = (caracter >> bit_pos) & 1
            col.append(bit)
            
        # Desplazamos 1 SOLA posición para hacerle lugar al nuevo bit de paridad
        ultimaFila = (ultimaFila << 1) | calculoParidadLista(col)

    ultimaFila = ultimaFila<<8*len(cadena)
    locura = ultimaFila|locura    

    return bin(locura)