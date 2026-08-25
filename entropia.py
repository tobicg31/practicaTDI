import informacion
import math
import random
    
def Entropia(P, I):
    H = 0
    for i in range(len(P)):
        H += P[i-1] * I[i-1]
    return H


"""ingresa una cadena y devuelve el alfabeto y sus probabilidades"""
def devuelveAlfabetoyProbs(cadena): 
    alfabeto = []
    probabilidades = []
    cont=[]
    for i in range(len(cadena)):
        if alfabeto.count(cadena[i]) == 0:
            alfabeto.append(cadena[i])
            probabilidades.append(1)
            cont.append(0)
        cont[alfabeto.index(cadena[i])] += 1

    for i in range(len(cont)):
        probabilidades[i] = cont[i] / len(cadena)
    return alfabeto, probabilidades

"""calcula la probabilidad acumulada de una lista de probabilidades"""
def probAcumulada(prob):
    acum = []
    acum.append(prob[0])
    for i in range(1,len(prob)):
        acum.append(acum[i-1]+prob[i])
    return acum

"""busco en la prob acumulada un valor en especifico y devuelvo el indice"""
def buscoAcum(acum, valor):
    i=0
    while (acum[i]<valor):
        i += 1
    return int(i-1)


"""dado un alfabeto y sus probabilidades, devuelve una cadena de longitud N en base a ese alfabeto y probs"""
def simularCadenaN(N, alfabeto, prob):
    acum = probAcumulada(prob)
    cadena = ""
    for i in range(N):
        c = alfabeto[buscoAcum(acum, random.random())]
        cadena+=c
    return cadena


if __name__ == "__main__":
    alfabeto, prob = devuelveAlfabetoyProbs("holaholas")
    cadena = simularCadenaN(8, alfabeto, prob)
    print(cadena)






'''
def binH(w,nw):
    return w*informacion.inf(w) + nw*informacion.inf(nw)

def equisH(n):
    return math.log2(n)

def extH(H, n):
    return n*H

print(f"La entropia es: {entropia(P,H)} bits")
'''