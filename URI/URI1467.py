def checker(lista):
    out='*'
    if lista[0]==lista[1] and lista[1]==lista[2]:
        pass
    else:
        if lista[0]==lista[1]:
            out='C'
        elif lista[0]==lista[2]:
            out='B'
        else:
            out='A' 
    return out

while True:
  try:
    line = input()
    line=line.split()
    vencedor = checker(line)
    print(vencedor)
  except EOFError:
    break