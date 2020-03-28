dimensions = [int(x) for x in input().split()]
matrix = []
somas = []
for i in range(dimensions[0]):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for line in matrix:
    somas.append(sum(line))

for k in range(dimensions[1]):
    col_sum = 0
    for line in matrix:
        col_sum += line[k]
    somas.append(col_sum)

print(max(somas))