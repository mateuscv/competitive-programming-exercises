# -*- coding: utf-8 -*-

while True:
	try:
		i,j = list(map(int, input().strip().split(" ")))
		
		soma = 0
		for x in range(i):
			vetor = list(map(int, input().strip().split(" ")))
			soma += sum(vetor)
			
		sacas = soma // 60
		litros = soma - (sacas * 60)
		
		print("%i saca(s) e %i litro(s)" %(sacas, litros))
		
	except EOFError:
		break
