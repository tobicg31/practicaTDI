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