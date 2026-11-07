import math

def informacion(p):
    if p >0:
        return math.log2(1/p)
    else:
        return 0

def probabilidades(largo, P):
    for i in range(largo):
        prob = float(input("Ingrese una probabilidad: "))
        P.append(prob) 

def listaInformacion(P):
    I=[]
    for i in range(len(P)):
        I.append(informacion(P[i]))
    return I



if __name__ == "__main__":
    print("hola")