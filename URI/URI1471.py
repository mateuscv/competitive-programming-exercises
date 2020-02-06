while True:
    try:
        line = input()
        line = line.split()
        line = [int(x) for x in line]

        retornaram = input()
        retornaram = retornaram.split()
        retornaram = [int(x) for x in retornaram]

        mergulhadores = list(range(1, line[0]+1))

        cont = 0
        mortos = []
        for mergulhador in mergulhadores:
            if mergulhador not in retornaram:
                cont+=1
                mortos.append(mergulhador)
        if cont == 0:
            print('* ')
        else:
            [print(str(x) + " ", end='') for x in mortos]
            print()
    except EOFError:
        break
