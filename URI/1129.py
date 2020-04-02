def check_letter(item, line):
    if line.index(item) == 0:
        return 'A'
    if line.index(item) == 1:
        return 'B'
    if line.index(item) == 2:
        return 'C'
    if line.index(item) == 3:
        return 'D'
    if line.index(item) == 4:
        return 'E'


cases = int(input())
while cases!=0:
    for i in range(cases):
        line = [int(x) for x in input().split()]
        contmarcados = 0
        for item in line:
            if item <= 127:
                contmarcados += 1
                letra = check_letter(item, line)
        if contmarcados == 1:
            print(letra)
        else:
            print("*")
    cases = int(input())