N = int(input())
H = [int(x) for x in input().split()]

nlogonia = "1"

for i in range(N-1):
    if H[i] == H[i+1]:
        nlogonia = "0"
        break
    if i !=0:
        if (H[i] >= H[i-1] and H[i] <= H[i+1]) or (H[i] <= H[i-1] and H[i] >= H[i+1]):
            nlogonia = "0"
            break

print(nlogonia)