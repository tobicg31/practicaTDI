def esNoSingular(codigo):
    f = True
    i=0
    j=0
    while (f and j < len(codigo)):
        while (f and i < len(codigo)):
            if (j != i):
                f = codigo[j] != codigo[i]
            i+=1
        j+=1
    return f

def EstaEnC(S, codigo):
    i = 0
    while ((i < len(codigo)) and (S[i] != codigo[i])):
        i+=1
    return i == len(codigo)

def esUnivocamente(codigo):
    S1 = codigo
    S2 = []

    while(S1 != S2 or not(EstaEnC(S2, codigo))):
        for i in range(len(codigo)):
            x = codigo[i]
            for j in range(len(codigo)):
                y = codigo[j]
                if x != y:
                    if y.startswith(x):
                        S2.append(y)
        S1 = S2
        S2 = []

    if (S1 == S2):
        return True
    if (EstaEnC(S2, codigo)):
        return False