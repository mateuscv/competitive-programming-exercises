linha = input().split()
linha = [int(x) for x in linha]
if (linha[0] == linha [1] or linha[0] == linha[2] or linha[1] == linha[2]) or ((linha[0] + linha[1]) == linha[2] or (linha[1]+linha[2]) == linha[0] or (linha[0] + linha[2]) == linha[1]):
    print("S")
else:
    print("N")