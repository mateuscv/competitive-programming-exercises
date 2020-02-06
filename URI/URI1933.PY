line = input()
line = line.split()
line = [int(x) for x in line]
if line[0]==line[1]:
    print(line[0])
elif line[0]>line[1]:
    print(line[0])
else:
    print(line[1])