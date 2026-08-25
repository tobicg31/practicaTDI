import math

def inf(p):
    return math.log2(1/p)

def probabilidades(largo, P):
    for i in range(largo):
        prob = float(input("Ingrese una probabilidad: "))
        P.append(prob) 

def listainformacion(P):
    I=[]
    for i in range(len(P)):
        I.append(inf(P))
    return I



if __name__ == "__main__":
    print("hola")