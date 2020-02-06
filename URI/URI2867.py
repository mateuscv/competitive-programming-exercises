# -*- coding: utf-8 -*-

casos = int(input())
	
for i in range(casos):
	n, m = list(map(int, input().strip().split(" ")))
	
	valor = str(n ** m)
	print(len(valor))
