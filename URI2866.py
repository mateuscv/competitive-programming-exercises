# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
	palavra = list(input())
	secreta = []
	for i in range(len(palavra)):
		nr = ord(palavra[i])
		if nr <= 90:
			continue
		
		secreta.insert(0, palavra[i])
		
	if secreta != []:
		print("".join(secreta))
