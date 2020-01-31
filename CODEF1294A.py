testCases = int(input())
for case in range(testCases):
    abcn = [int(x) for x in input().split()]
    summ = sum(abcn)
    if summ % 3 == 0 and (summ/3 >= max([abcn[0], abcn[1], abcn[2]])):
        print("YES")
    else:
        print("NO")
