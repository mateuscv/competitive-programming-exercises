from collections import Counter

N = int(input())
vars = []
for i in range(N):
    vars.append(int(input()))
contados = Counter(vars)
contados = sorted(contados.items())
for tupla in contados:
    print(str(tupla[0]) + " aparece " + str(tupla[1]) + " vez(es)")