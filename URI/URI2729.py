n = int(input())
for i in range(n):
		line = input().split()
		line = set(line)
		line = list(line)
		line.sort()
		print(" ".join(line))

