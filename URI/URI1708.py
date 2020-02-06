line = input().split()
line = [int(x) for x in line]
retardatario = False
contvoltas=1
rapidooriginal = line[0]
lentooriginal = line[1]
while retardatario is False:
    contvoltas+=1
    line[0] = line[0] + rapidooriginal
    line[1] = line[1] + lentooriginal
    if (line[1]-line[0]) >= lentooriginal:
        retardatario = True
        break
print(contvoltas)