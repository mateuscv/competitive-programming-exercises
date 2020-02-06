K = int(input())
while K!=0:
    linha = input().split()
    linha = [int(x) for x in linha]
    for i in range(K):
        coords = input().split()
        coords = [int(x) for x in coords]
        if coords[0] == linha[0] or coords[1] == linha[1]:
            print("divisa")
        elif coords[0] >= linha[0] and coords[1] >= linha[1]:
            print("NE")
        elif coords[0] <= linha[0] and coords[1] <= linha[1]:
            print("SO")
        elif coords[0] <= linha[0] and coords[1] >= linha[1]:
            print("NO")
        elif coords[0] >= linha[0] and coords[1] <= linha[1]:
            print("SE")
    K = int(input())