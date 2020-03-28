frase = input().split()
newfrase = ''
for i in range(len(frase)):
    newword = ''
    for j in range(len(frase[i])):
        if j%2 == 0:
            pass
        else:
            newword += frase[i][j]
    newfrase = newfrase + " " + newword
print(newfrase.strip())