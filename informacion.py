import math

def informacion(p):
    return math.log2(1/p)

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