while True:
    try:
        line = [int(x) for x in input().split()]

        dist_guarita_fugitivo = line[0]
        vel_fugitivo = line[1]
        vel_guarita = line[2]

        dist_guarita = ((12**2) + (dist_guarita_fugitivo**2))**0.5
        tempo_fugitivo = (12/vel_fugitivo)
        tempo_guarita = dist_guarita/vel_guarita

        if tempo_guarita <= tempo_fugitivo:
            print('S')
        else:
            print('N')
    except EOFError:
        break