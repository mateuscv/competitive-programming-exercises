n_amostras=int(input())
while n_amostras != 0:
    linha = input()
    amostras = linha.split()
    amostras = [int(x) for x in amostras]
    picos = 0
    for i in range(len(amostras)):
        if ((len(amostras) - i)>1 and i != 0):
            if ((amostras[i] > amostras[i-1] and amostras[i] > amostras[i+1]) or (amostras[i] < amostras[i-1] and amostras[i] < amostras[i+1])):
                picos+=1
    if ((amostras[-1] < amostras[0]) and (amostras[0] > amostras[1]) and (amostras[-1] < amostras[-2])) or (
        (amostras[-1] > amostras[0]) and (amostras[0] < amostras[1]) and (amostras[-1] > amostras[-2])):
        picos+=2
    else:
        picos+=1
    print(picos)
    n_amostras=int(input())
