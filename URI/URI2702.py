line1 = [int(x) for x in input().split()]
line2 = [int(x) for x in input().split()]

listaValores = []
soma = 0
for i in range(len(line1)):
	a = line2[i]-line1[i]
	if a > 0:
		soma += a

print(soma)
	

	
