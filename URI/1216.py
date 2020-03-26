totaldists = []

while(True):
    try:
        nome = input()
    except EOFError:
        break
    dist = float(input())
    totaldists.append(dist)

finaldist = sum(totaldists)
media = finaldist/len(totaldists)
print('{:.1f}'.format(media))