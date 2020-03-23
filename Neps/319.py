V_T = [int(x) for x in input().split()]
trocas = [int(x) for x in input().split()]

for i in range(V_T[1]):
    V_T[0] += trocas[i]
    if V_T[0] > 100:
        V_T[0] = 100
    if V_T[0] < 0:
        V_T[0] = 0

print(V_T[0])