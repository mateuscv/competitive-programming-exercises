N = input()
str1 = list(input())
str2 = list(input())

x = zip(str1, str2)

acertos = 0
for tuple in list(x):
    if tuple[0] == tuple[1]:
        acertos += 1

print(acertos)