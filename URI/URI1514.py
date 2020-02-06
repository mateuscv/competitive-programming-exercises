N_M = input().split()

#loop cada caso:

while N_M != ["0","0"]:
    N_M = [int(x) for x in N_M]
    numero_sol_problemas = [0]*N_M[1]
    criterio_1 = True
    criterio_2 = False
    criterio_3 = True
    criterio_4 = True
    
    matriz_problemas_participantes = []

    #loop cada participante:
    for i in range(N_M[0]):
        participante_problemas = [int(x) for x in input().split()]
        matriz_problemas_participantes.append(participante_problemas)

        for i in range(N_M[1]):
                if participante_problemas[i] == 1:
                    numero_sol_problemas[i] += 1
        
        #criterio 1:
        if (criterio_1) is True and (not 0 in participante_problemas):
            criterio_1 = False

        #criterio 2:
        if criterio_2 == False and not 0 in numero_sol_problemas:
            criterio_2 = True

        #criterio 3:
        if criterio_3 == True and N_M[0] in numero_sol_problemas:
            criterio_3 = False

        #criterio 4:
        participante_problemas_set = list(set(participante_problemas))
        if (criterio_4 == True) and (participante_problemas_set[0]) == 0 and len(participante_problemas_set)==1:
            criterio_4 = False
    
    cont_crit = 0
    if criterio_1 is True:
        cont_crit += 1
    if criterio_2 is True:
        cont_crit += 1
    if criterio_3 is True:
        cont_crit += 1
    if criterio_4 is True:
        cont_crit += 1

    print(cont_crit)

    N_M = input().split()
