NCS = input().split()
NCS = [int(x) for x in NCS]
N = NCS[0]
C = NCS[1]
S = NCS[2]

dicio = {}
for i in range(N):
    dicio[i+1] = 0

comandos = input().split()
atual = 1
dicio[1] = 1
for comando in comandos:
    if comando == '1':
        atual += 1
        if atual > N:
            atual = 1
        dicio[atual] += 1
    else:
        atual -= 1
        if atual <= 0:
            atual = N
        dicio[atual] += 1

print(dicio[S])