import copy

line = input()
while line!="0 0":
    A = input()
    B = input()
    A = [int(x) for x in A.split()]
    B = [int(x) for x in B.split()]
    A = list(dict.fromkeys(A))
    B = list(dict.fromkeys(B))
    A = set(A)
    B = set(B)
    oldA = copy.deepcopy(A)
    A = A-B
    B = B-oldA
    XOR = A ^ B
    tam_XOR = len(XOR)
    tam_A = len(A)
    tam_B = len(B)
    if tam_A > tam_B:
        menor = tam_B
    else:
        menor = tam_A
    if menor < tam_XOR:
        print(menor)
    else:
        print(tam_XOR)
    line = input()