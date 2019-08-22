# -*- coding: utf-8 -*-

from math import floor
t = int(input())

for i in range(t):
	n, k = list(map(int, input().split(" ")))
	res = floor(n/k) + (n % k)
	print(res)
